# aiagents/agents/backend_developer_agent.py

from aiagents.base.base_agent import BaseAgent
from crewai import Task
from aiagents.utils.file_writer import write_code_file
from aiagents.utils.path_utils import resolve_output_path


class BackendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BackendDeveloperAgent",
            role="Backend Developer",
            goal="Build the backend application logic, including APIs, models, and configurations.",
            backstory=(
                "You are a backend expert. You take architectural blueprints and prompt-engineered "
                "descriptions to build robust and scalable backend systems using technologies such as "
                "Node.js, Express, Flask, Django, or Spring Boot."
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

        filename = self._extract_filename_from_prompt(prompt) or "server.js"
        file_path = resolve_output_path(filename)

        write_code_file(file_path, result)

        return {"file": file_path, "status": "backend code generated"}

    def _extract_filename_from_prompt(self, prompt: str) -> str:
        import re
        match = re.search(r"generate\s+([\w\-/]+\.js)", prompt)
        return match.group(1) if match else None
