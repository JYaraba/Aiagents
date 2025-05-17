# backend/agents/agent_coordinator.py

from backend.agents.planner_agent import PlannerAgent
from backend.agents.prompt_engineer_agent import PromptEngineerAgent
from backend.agents.python_developer_agent import PythonDeveloperAgent
from backend.agents.frontend_developer_agent import FrontendDeveloperAgent
from backend.agents.ux_designer_agent import UXDesignerAgent
from backend.agents.fullstack_integrator_agent import FullStackIntegratorAgent
from backend.agents.tester_agent import TesterAgent
from backend.agents.bug_fixer_agent import BugFixerAgent
from backend.agents.packager_agent import PackagerAgent

def plan_and_build(user_prompt: str) -> dict:
    planner = PlannerAgent()
    prompt_engineer = PromptEngineerAgent()
    tester = TesterAgent()
    bug_fixer = BugFixerAgent()
    packager = PackagerAgent()

    # Step 1: Plan the tasks
    steps = planner.execute(user_prompt)

    # Step 2: Route each step to correct specialist via prompt engineer
    output_files = {}

    for step in steps:
        step_lower = step.lower()
        target_agent = ""

        if any(word in step_lower for word in ["backend", "api", "database", "python"]):
            target_agent = "PythonDeveloperAgent"
            prompt = prompt_engineer.execute({"task": step, "target_agent": target_agent})
            dev = PythonDeveloperAgent()
            output_files.update(dev.execute(prompt))

        elif any(word in step_lower for word in ["frontend", "html", "css", "react"]):
            target_agent = "FrontendDeveloperAgent"
            prompt = prompt_engineer.execute({"task": step, "target_agent": target_agent})
            dev = FrontendDeveloperAgent()
            output_files.update(dev.execute(prompt))

        elif any(word in step_lower for word in ["layout", "user interface", "flow"]):
            target_agent = "UXDesignerAgent"
            prompt = prompt_engineer.execute({"task": step, "target_agent": target_agent})
            dev = UXDesignerAgent()
            layout_plan = dev.execute(prompt)
            output_files["layout_plan.txt"] = layout_plan

        elif any(word in step_lower for word in ["connect", "integrate", "hook up"]):
            target_agent = "FullStackIntegratorAgent"
            prompt = prompt_engineer.execute({"task": step, "target_agent": target_agent})
            dev = FullStackIntegratorAgent()
            output_files.update(dev.execute(prompt))

    # Step 3: Run tests
    test_result = tester.execute(list(output_files.keys()))

    # Step 4: Fix any bugs
    if any("❌" in r for r in test_result["test_results"]):
        fixed = bug_fixer.execute(test_result["test_results"])
        output_files.update(fixed)

    # Step 5: Package the build
    package = packager.execute([])

    return {
        "tasks": steps,
        "test_results": test_result["test_results"],
        "package_path": package["zip_path"]
    }
