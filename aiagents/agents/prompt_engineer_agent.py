from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class PromptEngineerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PromptEngineerAgent",
            role="Prompt Engineer",
            goal="Craft optimized prompts for LLM interactions to maximize task accuracy and output relevance.",
            backstory=(
                "As the Prompt Engineer, your role is to transform vague goals into clear, actionable, and efficient prompts. "
                "You analyze requirements and use prompt tuning techniques to get the best results from large language models."
            )
        )

    @log_progress_step("PromptEngineerAgent", "Optimizing prompts for task execution")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": "PromptEngineerAgent",
            "details": "Prompt generated or optimized."
        }
