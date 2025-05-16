from .base_agent import BaseAgent
from backend.utils.progress_tracker import log_progress_step
from openai import OpenAI
from backend.config import settings
import os
from dotenv import load_dotenv

load_dotenv()

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="TesterAgent", role="QA Tester")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @log_progress_step("TesterAgent", "Tester Agent is executing")
    def execute(self, task_list: list[str]) -> dict:
        prompt = "\n".join(task_list)
        qa_prompt = (
            "You are a QA tester. Review the following development tasks and identify any missing functionality or test cases:\n\n"
            f"{prompt}"
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a QA tester."},
                {"role": "user", "content": qa_prompt}
            ],
            temperature=0.3
        )

        result = response.choices[0].message.content.strip()
        self.remember("last_test", result)

        return {
            "summary": result,
            "issues": [result]
        }
