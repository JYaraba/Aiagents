# backend/agents/fullstack_integrator_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import write_code_file
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
        Returns: Dict of filenames and generated glue code
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior full-stack developer. Connect frontend components with backend logic. Output just the glue code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        glue_code = response.choices[0].message.content.strip()

        # Derive target filename (improved handling can use metadata later)
        filename = "client/src/api/integrated_component.js"
        write_code_file(filename, glue_code)

        files = {filename: glue_code}
        self.remember("last_integration", files)
        return files
