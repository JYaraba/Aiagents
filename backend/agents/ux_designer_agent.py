# backend/agents/ux_designer_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os

load_dotenv()

class UXDesignerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="UXDesignerAgent", role="User Experience Designer")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("UXDesignerAgent", "Designing UX layout")
    def execute(self, feature_request: str) -> str:
        """
        feature_request: Description of what the user wants (e.g., "Login screen with password reset")
        Returns: A UX layout plan (not code, just layout description)
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a UX designer creating layout blueprints and user interaction flows."},
                {"role": "user", "content": f"Design the user experience layout and flow for the following request:\n\n{feature_request}"}
            ],
            temperature=0.4
        )

        layout_plan = response.choices[0].message.content.strip()
        self.remember("last_layout_plan", layout_plan)
        return layout_plan
