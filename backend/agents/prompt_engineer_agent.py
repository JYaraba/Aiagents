# backend/agents/agent_coordinator.py

from backend.agents.base_agent import BaseAgent
from backend.utils.progress_tracker import log_progress_step
from typing import Union
from backend.agents.architect_agent import ArchitectAgent
from backend.agents.planner_agent import PlannerAgent
from backend.agents.prompt_engineer_agent import PromptEngineerAgent
from backend.agents.frontend_developer_agent import FrontendDeveloperAgent
from backend.agents.nodejs_developer_agent import NodeJsDeveloperAgent
from backend.agents.ux_designer_agent import UXDesignerAgent
from backend.agents.fullstack_integrator_agent import FullStackIntegratorAgent
from backend.agents.tester_agent import TesterAgent
from backend.agents.bug_fixer_agent import BugFixerAgent
from backend.agents.packager_agent import PackagerAgent

from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import write_preview_file


@track_progress_step("AgentCoordinator", "Planning and building project")
def plan_and_build(prompt: str) -> dict:
    # 1. Analyze architecture
    architect = ArchitectAgent()
    architecture = architect.execute(prompt)

    if not isinstance(architecture, dict) or "stack" not in architecture:
        return {"error": "Failed to parse architect output"}

    # 2. Generate execution tasks
    planner = PlannerAgent()
    tasks = planner.execute(prompt)

    # 3. Generate engineered prompt
    prompt_engineer = PromptEngineerAgent()
    engineered_prompt = prompt_engineer.execute(prompt)

    # 4. Frontend code generation
    frontend_agent = FrontendDeveloperAgent()
    frontend_result = frontend_agent.execute(engineered_prompt)

    # 5. Backend code generation
    backend_agent = NodeJsDeveloperAgent()
    backend_result = backend_agent.execute(engineered_prompt)

    # ✅ 6. Generate preview HTML after backend generation
    write_preview_file("preview.html", title="App Preview", body="The application frontend has been successfully generated.")

    # 7. UX Design
    ux_agent = UXDesignerAgent()
    ux_result = ux_agent.execute(prompt)

    # 8. Integrate full stack
    integrator = FullStackIntegratorAgent()
    integration_result = integrator.execute(prompt)

    # 9. Run tests
    tester = TesterAgent()
    test_results = tester.execute([])

    # 10. Fix bugs if found
    bugfixer = BugFixerAgent()
    bugfix_result = bugfixer.execute(test_results)

    # 11. Package output
    packager = PackagerAgent()
    package_result = packager.execute(prompt)

    return {
        "architecture": architecture,
        "tasks": tasks,
        "test_results": test_results,
        "package_path": package_result.get("package_path")
    }
