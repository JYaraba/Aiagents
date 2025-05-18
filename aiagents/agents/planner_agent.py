from ..agents.base_agent import BaseAgent
from ..utils.progress_logger import log_step

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent")

    @log_step
    def execute(self, prompt: str) -> dict:
        print(f"[{self.name}] ➤ Planning execution steps")
        # Implementation logic here
        return {"plan": ["Step 1", "Step 2"]}
