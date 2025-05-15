from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress
from backend.utils.file_writer import write_code_to_project_structure, zip_output_folder
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os
load_dotenv()


class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DeveloperAgent", role="Code Generator")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress("Developer Agent is executing")
    def execute(self, task_list: list[str]) -> dict:
        prompt = "\n".join(task_list)
        dev_prompt = (
            "You are a senior developer. Write clean and well-documented code based on the following tasks:\n\n"
            f"{prompt}"
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior developer."},
                {"role": "user", "content": dev_prompt}
            ],
            temperature=0.3
        )

        code = response.choices[0].message.content.strip()
        files = {"main.py": code}
        self.remember("last_code", files)
        return files
