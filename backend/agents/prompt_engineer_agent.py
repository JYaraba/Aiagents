# backend/agents/prompt_engineer_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step

class PromptEngineerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PromptEngineerAgent", role="Prompt Generator")

    @track_progress_step("PromptEngineerAgent", "Generating role-specific prompt")
    def execute(self, task: dict) -> str:
        """
        Expected input format:
        {
            "task": "Build a login API using FastAPI",
            "target_agent": "PythonDeveloperAgent"
        }
        """
        raw_task = task.get("task", "")
        target = task.get("target_agent", "").lower()

        # Prompt template per agent
        if "python" in target:
            prompt = (
                "You are a Python backend engineer. Your task is:\n\n"
                f"{raw_task}\n\n"
                "Please write clean, well-commented Python code using FastAPI or relevant framework. "
                "Ensure syntax is valid and the file can be executed as-is."
            )
        elif "frontend" in target:
            prompt = (
                "You are a frontend developer. Your task is:\n\n"
                f"{raw_task}\n\n"
                "Generate responsive HTML/CSS or React code based on the description. Use functional components and basic styling."
            )
        elif "ux" in target:
            prompt = (
                "You are a UX designer. Your task is:\n\n"
                f"{raw_task}\n\n"
                "Describe a layout blueprint including user flow, sections, and interaction behaviors."
            )
        elif "fullstack" in target:
            prompt = (
                "You are a full-stack developer. Your task is:\n\n"
                f"{raw_task}\n\n"
                "Make sure frontend and backend connect properly using correct API routes and methods."
            )
        elif "bugfix" in target:
            prompt = (
                "You are a bug fixer. The code has a reported issue:\n\n"
                f"{raw_task}\n\n"
                "Identify the problem and rewrite the faulty line or section. Return only the fixed code."
            )
        else:
            prompt = f"You are a software engineer. Your task is:\n\n{raw_task}"

        self.remember("last_prompt", prompt)
        return prompt
