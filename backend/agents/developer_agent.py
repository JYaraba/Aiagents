from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import write_code_to_project_structure, zip_output_folder
from openai import OpenAI
from backend.config import settings
from dotenv import load_dotenv
import os
import re

load_dotenv()

class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="DeveloperAgent", role="Code Generator")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @track_progress_step("DeveloperAgent", "Developer Agent is executing")
    def execute(self, task_list: list[str]) -> dict:
        test_results = []
        tasks = []
        for item in task_list:
            if "❌ Syntax Error" in item:
                test_results.append(item)
            else:
                tasks.append(item)

        if test_results:
            print("[DeveloperAgent] Detected test errors. Attempting to fix...")

            for error in test_results:
                match = re.search(r"^(.*): ❌ Syntax Error - .*\(<unknown>, line (\d+)\)", error)
                print(f"[DeveloperAgent] Match found: {match.groups() if match else 'None'}")

                if match:
                    file_path, line_number = match.group(1), int(match.group(2))
                    full_path = os.path.join("output_projects", os.path.basename(file_path))

                    if os.path.exists(full_path):
                        with open(full_path, "r") as f:
                            lines = f.readlines()

                        if 0 < line_number <= len(lines):
                            print(f"[DeveloperAgent] Removing faulty line {line_number} from {full_path}")
                            lines[line_number - 1] = "# [AUTO-FIXED] Removed line due to syntax error\n"

                            with open(full_path, "w") as f:
                                f.writelines(lines)

                        with open(full_path, "r") as f:
                            updated_code = f.read()
                        files = {os.path.basename(full_path): updated_code}
                        self.remember("last_code", files)
                        return files


        # Fallback: normal code generation
        prompt = "\n".join(tasks)
        dev_prompt = (
            "You are a senior developer. Write clean and well-documented code based on the following tasks:\n\n"
            f"{prompt}"
        )

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior developer."},
                {"role": "user", "content": dev_prompt}
            ],
            temperature=0.3
        )

        code = response.choices[0].message.content.strip()
        files = {"main.py": code}
        self.remember("last_code", files)
        return files
