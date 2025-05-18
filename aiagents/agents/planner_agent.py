from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_logger import log_step


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PlannerAgent",
            role="Execution Planner",
            goal="Break down the project into tasks and assign them to the right agents."
        )

    @log_step("PlannerAgent", "Planning execution steps")
    def execute(self, prompt: str) -> dict:
        # Retrieve architecture from memory (set by ArchitectAgent)
        architecture = self.recall("architecture")
        if not architecture:
            raise ValueError("No architecture found in memory. ArchitectAgent must run first.")

        tasks = []

        # High-level steps (simulated for now)
        tasks.extend([
            "Analyze user prompt and finalize tech stack",
            "Generate folder structure",
            "Generate frontend components: LoginForm, RegistrationForm, Dashboard, App.js, index.js",
            "Generate backend: User model, controller, routes, server setup",
            "Design UI layout and styling for pages",
            "Write tests for backend and frontend",
            "Fix any code errors detected during testing",
            "Generate preview and documentation",
            "Package the final app into a downloadable format"
        ])

        categorized_tasks = {
            "Prompt Engineer": ["Generate custom prompts per role based on the task"],
            "Frontend Developer": [
                "Build LoginForm, RegistrationForm, Dashboard components",
                "Set up App.js and routing"
            ],
            "Backend Developer": [
                "Create server.js, routes/userRoutes.js, controllers/userController.js",
                "Connect to MongoDB and configure Express"
            ],
            "UI/UX Designer": [
                "Design user interface layout and flow",
                "Define styling for all frontend components"
            ],
            "Tester": [
                "Run syntax and integration tests",
                "Validate backend API responses"
            ],
            "Bug Fixer": [
                "Fix syntax or runtime issues reported by TesterAgent"
            ],
            "Packager": [
                "Create a zipped folder of the build output",
                "Generate preview.html or README.md for final review"
            ],
            "Full Stack Integrator": [
                "Ensure all generated code files connect properly",
                "Render a working end-to-end app with backend + frontend"
            ]
        }

        self.remember("tasks", categorized_tasks)
        return categorized_tasks
