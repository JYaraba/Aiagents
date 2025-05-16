from backend.agents.tester_agent import TesterAgent
from backend.utils.progress_tracker import log_progress_step

def run_tester_agent(prompt: str) -> list[str]:
    log_progress_step("TesterAgent", "Starting tests")
    tester = TesterAgent()
    result = tester.execute([prompt])
    log_progress_step("TesterAgent", f"Test results: {result['summary']}")
    return result["issues"]
