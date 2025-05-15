from .base_agent import BaseAgent
from openai import OpenAI
from backend.config import settings
from backend.utils.progress_tracker import log_progress_step
from dotenv import load_dotenv
import os
load_dotenv()


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent", role="Project Planner")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def execute(self, prompt: str) -> list[str]:
        planning_prompt = (
            f"You are a senior software architect. "
            f"Break down the following request into clear, step-by-step software development tasks:\n\n"
            f"{prompt}\n\n"
            f"Return the list of tasks in numbered format."
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a task planning assistant."},
                {"role": "user", "content": planning_prompt}
            ],
            temperature=0.4
        )

        output = response.choices[0].message.content.strip()
        steps = [line.strip() for line in output.split('\n') if line.strip()]
        log_progress_step(self.name, "Planning completed", steps)
        self.remember("last_plan", steps)
        return steps
