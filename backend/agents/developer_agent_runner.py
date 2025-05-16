from .developer_agent import DeveloperAgent
from backend.utils.progress_tracker import log_progress_step
from backend.langgraph.memory.hybrid_memory import memory_manager

def run_developer_agent(tasks: list[str]) -> dict:
    log_progress_step("DeveloperAgent", "Developer Agent is executing")
    dev = DeveloperAgent()
    code = dev.execute(tasks)
    memory_manager.save("last_dev_output", code)
    return code

def fix_failed_tasks_from_tests() -> dict:
    feedback = memory_manager.load("TesterAgent_last_test_issues")
    if not feedback:
        log_progress_step("DeveloperAgent", "No issues to fix from tests.")
        return {}

    log_progress_step("DeveloperAgent", f"Fixing issues from test feedback: {feedback}")
    return run_developer_agent(feedback)
