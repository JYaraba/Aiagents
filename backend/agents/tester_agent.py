from .base_agent import BaseAgent
from backend.utils.progress_tracker import log_progress_step
from backend.utils.file_writer import load_python_files
from typing import List
import ast


class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="TesterAgent", role="Functionality Validator")

    @log_progress_step("TesterAgent", "Tester Agent is executing")
    def execute(self, task_list: List[str]) -> dict:
        log_progress_step(self.name, "Tester Agent is executing")

        test_results = []
        files_to_test = load_python_files("output_projects")

        for file_path, content in files_to_test.items():
            try:
                ast.parse(content)
                test_results.append(f"{file_path}: ✅ Syntax OK")
            except SyntaxError as e:
                test_results.append(f"{file_path}: ❌ Syntax Error - {e}")

        self.remember("test_results", test_results)
        return {"test_results": test_results}
