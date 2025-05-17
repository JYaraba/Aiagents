# backend/agents/agent_coordinator.py

from backend.agents.architect_agent import ArchitectAgent
from backend.agents.planner_agent import PlannerAgent
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
    # Step 1: Analyze architecture
    architect = ArchitectAgent()
    architecture = architect.execute(prompt)

    if not isinstance(architecture, dict) or "stack" not in architecture:
        return {"error": "Failed to parse architect output"}

    # Step 2: Generate project tasks
    planner = PlannerAgent()
    tasks = planner.execute(prompt)

    # Step 3: Use PromptEngineerAgent only inside this function to avoid circular import
    from backend.agents.prompt_engineer_agent import PromptEngineerAgent
    prompt_engineer = PromptEngineerAgent()
    engineered_prompt = prompt_engineer.execute(prompt)

    # Step 4: Frontend Developer builds UI
    frontend_dev = FrontendDeveloperAgent()
    frontend_result = frontend_dev.execute(engineered_prompt)

    # Step 5: Backend Developer builds server logic
    backend_dev = NodeJsDeveloperAgent()
    backend_result = backend_dev.execute(engineered_prompt)

    # ✅ Step 6: Generate preview.html after backend is done
    write_preview_file("preview.html", title="App Preview", body="The application frontend has been successfully generated.")

    # Step 7: UX Designer creates layout enhancements
    ux_agent = UXDesignerAgent()
    ux_result = ux_agent.execute(prompt)

    # Step 8: Full Stack Integrator merges everything
    integrator = FullStackIntegratorAgent()
    integration_result = integrator.execute(prompt)

    # Step 9: Tester Agent validates generated files
    tester = TesterAgent()
    test_result = tester.execute([])

    # Step 10: Bug Fixer Agent applies quick fixes
    bugfixer = BugFixerAgent()
    bugfix_result = bugfixer.execute(test_result)

    # Step 11: Packager Agent packages the build
    packager = PackagerAgent()
    package_result = packager.execute(prompt)

    return {
        "architecture": architecture,
        "tasks": tasks,
        "test_results": test_result,
        "package_path": package_result.get("package_path")
    }
