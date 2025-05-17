# backend/agents/nodejs_developer_agent.py

from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import write_code_to_project_structure


class NodeJsDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="NodeJsDeveloperAgent", role="Node.js Backend Developer")

    @track_progress_step("NodeJsDeveloperAgent", "Generating Node.js code")
    def execute(self, prompt: str) -> dict:
        # For now, assume prompt is already backend-specific
        file_map = {
            "create express server": "server.js",
            "define user model": "models/User.js",
            "create user routes": "routes/users.js",
        }

        generated_files = {}

        for desc, filename in file_map.items():
            if desc in prompt.lower():
                code = self.generate_code_block(prompt + f" — generate {filename}")
                output_path = f"output_projects/{filename}"
                write_code_to_project_structure({filename: code}, "output_projects")
                generated_files[filename] = code

        return generated_files

    def generate_code_block(self, prompt: str) -> str:
        system_prompt = (
            "You are a senior Node.js developer. Generate clean Express.js code with proper imports and exports. "
            "Only return code — no explanation."
        )
        response = self.llm.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
