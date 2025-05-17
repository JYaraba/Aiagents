# backend/agents/frontend_developer_agent.py

from backend.agents.base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import write_code_to_project_structure


class FrontendDeveloperAgent(BaseAgent):
    def __init__(self):
        # ✅ Ensure BaseAgent initializes the llm client
        super().__init__(name="FrontendDeveloperAgent", role="React Frontend Developer")

    @track_progress_step("FrontendDeveloperAgent", "Generating React UI code")
    def execute(self, prompt: str) -> dict:
        file_candidates = [
            "LoginForm.js", "Dashboard.js", "App.js", "RegistrationForm.js",
            "ProfilePage.js", "Navbar.js", "Sidebar.js", "SettingsForm.js"
        ]
        generated_files = {}

        for filename in file_candidates:
            base_name = filename.lower().replace(".js", "")
            if base_name in prompt.lower():
                if filename == "App.js":
                    path = f"client/src/{filename}"
                else:
                    path = f"client/src/components/{filename}"

                # ✅ LLM must be available here
                code = self.generate_code_block(prompt + f" — generate {filename}")
                write_code_to_project_structure({path: code}, "output_projects")
                generated_files[path] = code

        return generated_files

    def generate_code_block(self, prompt: str) -> str:
        system_prompt = (
            "You are a senior React developer. Generate clean functional React components using ES6. "
            "Use hooks where appropriate. Return code only, no explanations."
        )
        # ✅ Ensure self.llm exists from BaseAgent
        response = self.llm.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
