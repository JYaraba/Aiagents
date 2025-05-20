from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_output_file
from aiagents.utils.progress_tracker import log_progress_step


class FullStackIntegratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FullStackIntegratorAgent",
            role="Full Stack Integrator",
            goal="Integrate frontend and backend into a cohesive runnable application",
            backstory="Expert in gluing frontend and backend components, enabling a seamless development and runtime experience.",
        )

    @log_progress_step("FullStackIntegratorAgent", "Integrating frontend and backend")
    def execute(self, task_data: list | dict) -> dict:
        integration_code = """from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

todos = []

@app.route('/')
def serve_ui():
    return send_from_directory(app.static_folder, 'index.html')

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

        write_output_file("server.py", integration_code)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Created integration entry point: server.py"
        }
