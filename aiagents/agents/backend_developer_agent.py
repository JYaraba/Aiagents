from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_output_file
from aiagents.utils.progress_tracker import log_progress_step


class BackendDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BackendDeveloperAgent",
            role="Backend Engineer",
            goal="Create backend APIs using Flask to support frontend operations",
            backstory="Experienced in developing backend logic and RESTful APIs using Python and Flask.",
        )

    @log_progress_step("BackendDeveloperAgent", "Generating backend logic")
    def execute(self, task_data: list | dict) -> dict:
        # Basic Flask API setup for a to-do list
        flask_code = """from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todos.append(data['task'])
    return jsonify({'status': 'Task added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
"""

        # Write file
        write_output_file("backend/app.py", flask_code)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Backend file generated: app.py",
        }
