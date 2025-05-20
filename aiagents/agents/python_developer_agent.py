from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_output_file
from aiagents.utils.progress_tracker import log_progress_step


class PythonDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PythonDeveloperAgent",
            role="Flask Backend Developer",
            goal="Build Flask-based backend APIs to support the frontend",
            backstory="A backend engineer who specializes in building RESTful APIs and microservices using Flask for small and scalable applications."
        )

    @log_progress_step("PythonDeveloperAgent", "Generating Flask backend")
    def execute(self, task_data: list | dict) -> dict:
        # Create basic Flask server
        flask_app_code = """from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    task = data.get('task')
    if task:
        todos.append(task)
        return jsonify({'message': 'Task added'}), 201
    return jsonify({'error': 'Task is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
"""

        requirements = """flask==2.2.5"""

        write_output_file("flask_backend/app.py", flask_app_code)
        write_output_file("flask_backend/requirements.txt", requirements)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Flask backend generated successfully under flask_backend/."
        }
