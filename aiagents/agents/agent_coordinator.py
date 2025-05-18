import json
from aiagents.agents.architect_agent import ArchitectAgent
from aiagents.agents.planner_agent import PlannerAgent
from aiagents.agents.memory_agent import MemoryAgent
from crew.task_router import route_task
from backend.utils.file_writer import write_preview_file
from backend.utils.test_runner import run_code_tests
from backend.utils.progress_tracker import log_progress_step


@log_progress_step("AgentCoordinator", "Planning and building project")
def plan_and_build(app_prompt: str) -> dict:
    # Phase 1: Architecture & Planning
    architect = ArchitectAgent()
    architecture = architect.execute(app_prompt)

    if not isinstance(architecture, dict):
        raise ValueError("Invalid architecture format returned by ArchitectAgent.")

    planner = PlannerAgent()
    task_plan = planner.execute(app_prompt)

    if not isinstance(task_plan, list):
        raise ValueError("Invalid plan format returned by PlannerAgent.")

    # Store memory for reference
    memory = MemoryAgent()
    memory.store("architecture", architecture)
    memory.store("task_plan", task_plan)

    # Phase 2: Dynamic Task Execution
    task_outputs = []
    for task in task_plan:
        agent_name = task.get("agent")
        task_description = task.get("task")

        if not agent_name or not task_description:
            continue

        try:
            output = route_task(agent_name, task_description)
            task_outputs.append({"agent": agent_name, "task": task_description, "output": output})
        except Exception as e:
            task_outputs.append({"agent": agent_name, "task": task_description, "error": str(e)})

    # Phase 3: Testing
    test_results = run_code_tests()
    memory.store("test_results", test_results)

    # Phase 4: Preview Generation (UI)
    try:
        write_preview_file()
    except Exception as e:
        task_outputs.append({"agent": "PreviewWriter", "task": "Generate preview.html", "error": str(e)})

    # Phase 5: Final Output
    return {
        "architecture": architecture,
        "tasks": task_plan,
        "outputs": task_outputs,
        "test_results": test_results
    }
