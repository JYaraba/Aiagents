# backend/agents/planner_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent", role="Task Planner")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("PlannerAgent", "Planning execution steps")
    def execute(self, user_goal: str) -> list[str]:
        """
        user_goal: High-level objective (e.g., 'Build a login page')
        Returns: List of actionable steps to be executed by other agents
        """

        planning_prompt = (
            "You are a project planner AI. Break down the following high-level goal "
            "into clear, actionable software development steps that can be executed by AI developer agents.\n\n"
            f"Goal: {user_goal}\n\n"
            "List the steps as clear bullet points."
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior software planner."},
                {"role": "user", "content": planning_prompt}
            ],
            temperature=0.4
        )

        plan_raw = response.choices[0].message.content.strip()
        steps = [line.strip("-• ") for line in plan_raw.splitlines() if line.strip()]
        self.remember("last_plan", steps)
        return steps
