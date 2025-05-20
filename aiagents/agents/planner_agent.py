from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PlannerAgent",
            role="Planning Expert",
            goal="Break down the app goal into actionable development tasks.",
            backstory="You are a software planning expert skilled at analyzing user goals and converting them into structured engineering tasks."
        )

    @log_progress_step("PlannerAgent", "Planning and task breakdown")
    def execute(self, task_data):
        if isinstance(task_data, str):
            app_goal = task_data
        elif isinstance(task_data, dict):
            app_goal = task_data.get("app_goal", "Build a generic multi-agent application.")
        else:
            raise ValueError("Unsupported input type for PlannerAgent.execute")

        return [
            {"id": 1, "description": f"Analyze goal: {app_goal}"},
            {"id": 2, "description": "Design frontend layout"},
            {"id": 3, "description": "Generate backend Flask code"},
            {"id": 4, "description": "Integrate HTML, JS with Flask"},
        ]
