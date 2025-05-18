from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.utils.file_writer import write_json_file


class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent", role="Strategic Task Planner")

    @log_progress_step("PlannerAgent", "Planning execution steps")
    def execute(self, prompt: str) -> dict:
        """
        Plans out the execution strategy based on the input prompt.
        Returns a list of tasks and updates tasks.json.
        """
        planned_tasks = [
            {
                "agent": "UXDesignerAgent",
                "task": "Design a clean, intuitive user interface for the app described in the prompt."
            },
            {
                "agent": "PythonDeveloperAgent",
                "task": "Implement backend logic for user authentication and data management."
            },
            {
                "agent": "FrontendDeveloperAgent",
                "task": "Develop frontend components based on the UI design and connect to backend."
            },
            {
                "agent": "BugFixerAgent",
                "task": "Test the entire application and fix any bugs or inconsistencies."
            },
            {
                "agent": "FullStackIntegratorAgent",
                "task": "Integrate frontend and backend into a deployable application structure."
            }
        ]

        self.remember("planned_tasks", planned_tasks)
        write_json_file("output/tasks.json", planned_tasks)
        return {"tasks": planned_tasks}
