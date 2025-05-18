import os
from crewai_tools import FileReadTool, FileWriteTool
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.agents.base_agent import BaseAgent

class NodeJsDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="NodeJsDeveloperAgent",
            role="Backend Node.js Developer",
            goal="Build Node.js backend components based on planning tasks",
            tools=[FileReadTool(), FileWriteTool()]
        )

    @log_progress_step("NodeJsDeveloperAgent", "Generating Node.js backend files")
    def execute(self, task: str) -> dict:
        """
        Generate a simple Node.js Express backend file structure and code.
        """
        project_root = os.path.join("aiagents", "output", "nodejs_backend")
        os.makedirs(project_root, exist_ok=True)

        app_js_content = """\
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello from Node.js Backend!');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
"""
        package_json_content = """\
{
  "name": "aiagents-nodejs-backend",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
"""
        self.tools[1].write_file(os.path.join(project_root, "app.js"), app_js_content)
        self.tools[1].write_file(os.path.join(project_root, "package.json"), package_json_content)

        return {
            "status": "Node.js backend generated",
            "files": ["app.js", "package.json"],
            "output_dir": project_root
        }
