from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_logger import log_step


class ArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ArchitectAgent",
            role="Solution Architect",
            goal="Analyze the prompt and decide on the tech stack, folder structure, required agents, and base architecture plan."
        )

    @log_step("ArchitectAgent", "Analyzing app prompt and selecting tech stack")
    def execute(self, prompt: str) -> dict:
        # For now, simulate architecture generation. Later, this will use LLM output.
        architecture = {
            "stack": {
                "frontend": "React.js",
                "backend": "Node.js, Express.js",
                "database": "MongoDB",
                "devops": "Docker, AWS",
                "version_control": "Git"
            },
            "agents_needed": [
                "Prompt Engineer",
                "Frontend Developer",
                "Backend Developer",
                "UI/UX Designer",
                "Tester",
                "Bug Fixer",
                "Packager",
                "Full Stack Integrator"
            ],
            "folder_structure": {
                "root": {
                    "client": {
                        "public": {},
                        "src": {
                            "components": {
                                "LoginForm.js": {},
                                "RegistrationForm.js": {},
                                "Dashboard.js": {}
                            },
                            "App.js": {},
                            "index.js": {}
                        }
                    },
                    "server": {
                        "routes": {
                            "userRoutes.js": {}
                        },
                        "controllers": {
                            "userController.js": {}
                        },
                        "models": {
                            "User.js": {}
                        },
                        "server.js": {}
                    }
                }
            },
            "dependencies": {
                "npm": {
                    "client": [
                        "react", "react-dom", "axios", "react-router-dom"
                    ],
                    "server": [
                        "express", "cors", "body-parser", "mongoose", "bcrypt", "jsonwebtoken"
                    ]
                }
            }
        }

        self.remember("architecture", architecture)
        return architecture
