from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class BugFixerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BugFixerAgent",
            role="Bug Fixer",
            goal="Identify and resolve functional or logical bugs in generated code.",
            backstory=(
                "You are a detail-oriented bug fixer who reads logs, interprets error messages, and corrects code issues. "
                "Your job is to make sure nothing is broken in the application."
            )
        )

    @log_progress_step("BugFixerAgent", "Fixing bugs in logic or syntax")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": "BugFixerAgent",
            "details": "Task processed."
        }
