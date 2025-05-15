from .planner_agent import PlannerAgent
from backend.utils.progress_tracker import log_progress_step

def run_planner_agent(prompt: str) -> list[str]:
    planner = PlannerAgent()
    log_progress_step("PlannerAgent", "Starting planning")
    steps = planner.execute(prompt)
    log_progress_step("PlannerAgent", "Returned steps", steps)
    return steps
