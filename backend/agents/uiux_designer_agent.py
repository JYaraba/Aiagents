# aiagents/agents/uiux_designer_agent.py

from aiagents.base.base_agent import BaseAgent
from backend.utils.file_writer import write_code_file
from backend.utils.path_utils import resolve_output_path
from crewai import Task


class UIUXDesignerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="UIUXDesignerAgent",
            role="UI/UX Designer",
            goal="Design clear and accessible interfaces and user journeys for the application.",
            backstory=(
                "You are a seasoned UI/UX designer with experience in crafting user-friendly, accessible, "
                "and elegant interfaces. You produce layout plans, component suggestions, or high-level HTML mockups "
                "that can be handed off to frontend developers for implementation."
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

        filename = self._extract_filename(prompt) or "ui_layout_plan.md"
        file_path = resolve_output_path(filename)

        write_code_file(file_path, result)

        return {"file": file_path, "status": "ui/ux layout generated"}

    def _extract_filename(self, prompt: str) -> str:
        import re
        match = re.search(r"generate\s+([\w\-/]+(?:\.html|\.css|\.md))", prompt)
        return match.group(1) if match else None
