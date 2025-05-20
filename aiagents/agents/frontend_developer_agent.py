from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.utils.file_writer import write_output_file

class FrontendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FrontendDeveloperAgent",
            role="Frontend Developer",
            goal="Build beautiful and functional user interfaces.",
            backstory=(
                "You specialize in developing responsive and engaging user interfaces using HTML, CSS, and JavaScript frameworks. "
                "You ensure frontend components align with the UI/UX plan."
            )
        )

    @log_progress_step("FrontendDeveloperAgent", "Generating frontend components")
    def execute(self, task_data: dict) -> dict:
        html_content = "<!DOCTYPE html>\n<html>\n<head><title>To-Do App</title></head>\n<body>\n<h1>My To-Do List</h1>\n<ul id='tasks'></ul>\n<script src='app.js'></script>\n</body>\n</html>"
        js_content = "const tasks = ['Learn Python', 'Build a web app'];\nconst list = document.getElementById('tasks');\ntasks.forEach(task => { const li = document.createElement('li'); li.textContent = task; list.appendChild(li); });"

        write_output_file("output_projects/frontend/index.html", html_content)
        write_output_file("output_projects/frontend/app.js", js_content)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Frontend HTML and JS files generated."
        }
