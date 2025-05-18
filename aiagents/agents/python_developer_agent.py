import os
from crewai_tools import FileReadTool, FileWriteTool
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.agents.base_agent import BaseAgent

class PythonDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PythonDeveloperAgent",
            role="Python Backend Developer",
            goal="Generate Python-based backend services and utilities",
            tools=[FileReadTool(), FileWriteTool()]
        )

    @log_progress_step("PythonDeveloperAgent", "Creating Python backend structure")
    def execute(self, task: str) -> dict:
        """
        Generates a basic FastAPI backend structure.
        """
        project_root = os.path.join("aiagents", "output", "python_backend")
        os.makedirs(project_root, exist_ok=True)

        main_py_content = """\
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Python FastAPI backend!"}
"""

        requirements_txt = "fastapi\nuvicorn\n"

        self.tools[1].write_file(os.path.join(project_root, "main.py"), main_py_content)
        self.tools[1].write_file(os.path.join(project_root, "requirements.txt"), requirements_txt)

        return {
            "status": "Python FastAPI backend generated",
            "files": ["main.py", "requirements.txt"],
            "output_dir": project_root
        }
