from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_output_file
from aiagents.utils.progress_tracker import log_progress_step


class NodeJsDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="NodeJsDeveloperAgent",
            role="Node.js Backend Developer",
            goal="Generate Node.js backend logic using Express",
            backstory="Experienced Node.js engineer who builds robust REST APIs with Express and handles server-side tasks efficiently."
        )

    @log_progress_step("NodeJsDeveloperAgent", "Generating Node.js backend")
    def execute(self, task_data: list | dict) -> dict:
        # Generate server.js with Express API
        server_code = """const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

let todos = [];

app.get('/todos', (req, res) => {
  res.json(todos);
});

app.post('/todos', (req, res) => {
  const task = req.body.task;
  if (task) {
    todos.push(task);
    res.status(201).json({ message: 'Task added.' });
  } else {
    res.status(400).json({ error: 'Task is required.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
"""

        package_json = """{
  "name": "todo-node-api",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "body-parser": "^1.20.2"
  }
}
"""

        write_output_file("node_backend/server.js", server_code)
        write_output_file("node_backend/package.json", package_json)

        return {
            "status": "executed",
            "agent": self.name,
            "details": "Generated Node.js backend (Express) in node_backend/."
        }
