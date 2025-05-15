from .developer_agent import DeveloperAgent
from backend.utils.progress_tracker import log_progress_step

def run_developer_agent(tasks: list[str]) -> dict:
    developer = DeveloperAgent()
    log_progress_step("DeveloperAgent", "Starting development")
    code_files = developer.execute(tasks)
    log_progress_step("DeveloperAgent", "Code generated", list(code_files.keys()))
    return code_files
