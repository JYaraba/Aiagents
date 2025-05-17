# backend/agents/python_developer_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

class PythonDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PythonDeveloperAgent", role="Backend Developer")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("PythonDeveloperAgent", "Generating Python code")
    def execute(self, task_prompt: str) -> dict:
        """
        task_prompt: A clean, structured prompt from PromptEngineerAgent
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional Python backend developer."},
                {"role": "user", "content": task_prompt}
            ],
            temperature=0.3
        )

        code = response.choices[0].message.content.strip()

        # Default file target is main.py, can be customized later
        files = {"main.py": code}
        self.remember("last_code", files)
        return files
