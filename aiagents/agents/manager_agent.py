from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class ManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ManagerAgent",
            role="Project Manager",
            goal="Coordinate the AI agents and ensure timely completion of all tasks.",
            backstory="You are the Project Manager responsible for ensuring smooth task assignment, reviewing progress, and reporting the status of the application development process across all agents."
        )

    @log_progress_step("ManagerAgent", "Managing the workflow and agent coordination")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": self.name,
            "details": "Task processed."
        }
