# backend/agents/architect_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()


class ArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ArchitectAgent", role="Application Architect")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("ArchitectAgent", "Analyzing app prompt and selecting tech stack")
    def execute(self, user_prompt: str) -> dict:
        system_prompt = (
            "You are a senior software architect. Based on the following app idea, return only valid JSON with:\n"
            "- 'stack' (with keys: frontend, backend, devops, version_control)\n"
            "- 'agents_needed' (list of roles)\n"
            "- 'folder_structure' (nested structure of folders and files)\n"
            "- 'dependencies' (npm, pip, or others)\n\n"
            "Strictly return only the JSON — no explanation, markdown, or notes."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.3
            )

            content = response.choices[0].message.content.strip()

            # 🧹 Remove markdown fences if present (```json ... ```)
            if content.startswith("```json") or content.startswith("```"):
                content = re.sub(r"```(json)?", "", content).strip()

            # 🧪 Try to parse it
            result = json.loads(content)

            # ✅ Validate required keys
            required_keys = ["stack", "agents_needed", "folder_structure", "dependencies"]
            if not all(k in result for k in required_keys):
                return {"error": f"Missing required keys in architect output: {list(result.keys())}"}

            # 🧠 Memory save
            self.remember("selected_stack", result)
            return result

        except Exception as e:
            return {"error": f"Failed to parse architect output: {str(e)}"}
