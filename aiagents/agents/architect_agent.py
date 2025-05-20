# aiagents/agents/architect_agent.py

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class ArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ArchitectAgent",
            role="Solution Architect",
            goal="Design high-level system architecture and guide development planning.",
            backstory=(
                "You are a seasoned software architect. Your job is to understand the high-level goals of the project "
                "and define the best architecture, technology stack, and integration patterns. "
                "You collaborate closely with developers and planners to ensure scalability, performance, and maintainability."
            )
        )

    @log_progress_step("ArchitectAgent", "Creating high-level architecture")
    def execute(self, task_data: list) -> dict:
        # Convert list of task strings or dicts into a summarized description
        if isinstance(task_data, list):
            requirements = "\n".join(
                [f"- {task}" if isinstance(task, str) else f"- {task.get('description', str(task))}" for task in task_data]
            )
        else:
            requirements = str(task_data)

        tech_stack = "Node.js for backend, React for frontend, FastAPI for APIs, PostgreSQL for database"
        diagram = "Services → API Gateway → Backend (FastAPI/Node) → DB + Frontend (React)"

        architecture_plan = {
            "summary": "Designed modular and scalable architecture.",
            "tech_stack": tech_stack,
            "diagram": diagram,
            "notes": f"Generated based on:\n{requirements}"
        }

        self.remember("architecture_plan", architecture_plan)
        return architecture_plan
