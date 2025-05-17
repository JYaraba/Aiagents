# backend/agents/fullstack_integrator_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

class FullStackIntegratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="FullStackIntegratorAgent", role="Integration Specialist")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("FullStackIntegratorAgent", "Connecting frontend and backend")
    def execute(self, prompt: str) -> dict:
        """
        prompt: Integration-focused prompt from PromptEngineerAgent
        Returns: Dict of updated files or glue code (e.g., {"Login.js": "...updated..."})
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior full-stack developer. Connect frontend components with backend logic."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        glue_code = response.choices[0].message.content.strip()

        # Default return — in real cases, filenames may be inferred or passed in prompt
        files = {"integrated_component.js": glue_code}
        self.remember("last_integration", files)
        return files
