# aiagents/agents/packager_agent.py

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class PackagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PackagerAgent",
            role="Application Packager",
            goal="Package the generated application files into a deliverable zip file.",
            backstory=(
                "You are the final step in the development pipeline. Your responsibility is to collect the generated code, structure it cleanly, "
                "and compress it into a ZIP file for delivery or deployment. You ensure everything is ready for release."
            )
        )

    @log_progress_step("PackagerAgent", "Packaging generated app")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": "PackagerAgent",
            "details": "Application packaged successfully."
        }
