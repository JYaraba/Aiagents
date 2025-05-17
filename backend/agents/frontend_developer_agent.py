# backend/agents/frontend_developer_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

class FrontendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="FrontendDeveloperAgent", role="UI Builder")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("FrontendDeveloperAgent", "Generating frontend code")
    def execute(self, prompt: str) -> dict:
        """
        prompt: Frontend-specific prompt from PromptEngineerAgent
        Returns: Dict of files (e.g., {"Login.js": "...code..."})
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional frontend developer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        code = response.choices[0].message.content.strip()

        # By default, output to index.html unless prompt specifies filename (future enhancement)
        files = {"index.html": code}
        self.remember("last_ui_code", files)
        return files
