# aiagents/agents/frontend_developer_agent.py

from aiagents.base.base_agent import BaseAgent
from crewai import Task
from backend.utils.file_writer import write_code_file
from backend.utils.path_utils import resolve_output_path


class FrontendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FrontendDeveloperAgent",
            role="Frontend Developer",
            goal="Generate user interface code using modern frontend frameworks like React or Vue.",
            backstory=(
                "You are a frontend specialist responsible for implementing beautiful and functional UI "
                "based on structured prompts. Your task is to turn descriptions and component specs into actual code."
            )
        )

    def run(self, engineered_task: dict) -> dict:
        agent_role = engineered_task.get("agent", "")
        prompt = engineered_task.get("prompt", "")

        if agent_role != self.name:
            return {"skipped": True}

        task = Task(
            description=prompt,
            agent=self.agent
        )

        result = task.execute()

        # Optional: Extract filename from prompt or use convention
        filename = self._extract_filename_from_prompt(prompt) or "App.js"
        file_path = resolve_output_path(filename)

        write_code_file(file_path, result)

        return {"file": file_path, "status": "frontend code generated"}

    def _extract_filename_from_prompt(self, prompt: str) -> str:
        # Look for something like 'generate LoginForm.js' in the prompt
        import re
        match = re.search(r"generate\s+([\w\-/]+\.js)", prompt)
        return match.group(1) if match else None
