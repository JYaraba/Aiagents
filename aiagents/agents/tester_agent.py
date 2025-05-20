# aiagents/agents/tester_agent.py

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_logger import log_step
from aiagents.utils.test_runner import run_basic_syntax_tests

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TesterAgent",
            role="Functionality Validator",
            goal="Ensure that generated code is syntactically correct and logically sound before it is finalized.",
            backstory=(
                "You are the quality assurance expert in the AI agent team. You rigorously test all output from developer agents to catch errors "
                "early and maintain high reliability across the system. You validate correctness, structure, and readiness for deployment."
            )
        )

    def execute(self, task_data: dict) -> dict:
        log_step("TesterAgent", "Starting validation tests on output files")
        result = run_basic_syntax_tests(directory="output_projects")
        return {
            "status": "complete",
            "test_results": result
        }
