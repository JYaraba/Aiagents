from backend.agents.tester_agent import TesterAgent
from backend.utils.progress_tracker import log_progress_step

def run_tester_agent(prompt: str) -> list[str]:
    log_progress_step("TesterAgent", "Starting tests")
    
    tester = TesterAgent()
    result = tester.execute([prompt])

    # Safely log the test results
    log_progress_step("TesterAgent", "Test results", result["test_results"])

    return result["test_results"]
