from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class UIUXDesignerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="UIUXDesignerAgent",
            role="UI/UX Designer",
            goal="Design intuitive user interfaces and user experiences based on requirements.",
            backstory=(
                "You are a creative expert in visual and interaction design. You work closely with planners and developers to convert functional needs "
                "into beautiful, accessible, and intuitive user interfaces."
            )
        )

    @log_progress_step("UIUXDesignerAgent", "Designing UI/UX layouts")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": "UIUXDesignerAgent",
            "details": "UI/UX plan delivered."
        }
