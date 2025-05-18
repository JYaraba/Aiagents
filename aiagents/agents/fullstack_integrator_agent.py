# aiagents/agents/fullstack_integrator_agent.py

from aiagents.base.base_agent import BaseAgent
from backend.utils.file_writer import write_code_file
from backend.utils.path_utils import resolve_output_path
from crewai import Task


class FullStackIntegratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FullStackIntegratorAgent",
            role="Full Stack Integrator",
            goal="Integrate frontend and backend components into a functional full-stack application.",
            backstory=(
                "You are a full stack integrator who ensures frontend and backend work seamlessly together. "
                "You verify that the backend APIs are properly consumed by the frontend, environment configurations "
                "are aligned, and you generate glue code or documentation to tie the entire stack together."
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

        # Save integration summary or generated code
        filename = self._extract_filename(prompt) or "integration_notes.md"
        file_path = resolve_output_path(filename)

        write_code_file(file_path, result)

        return {"file": file_path, "status": "integration complete"}

    def _extract_filename(self, prompt: str) -> str:
        import re
        match = re.search(r"generate\s+([\w\-/]+(?:\.js|\.ts|\.md))", prompt)
        return match.group(1) if match else None
