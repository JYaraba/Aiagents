# backend/agents/tester_agent.py

import ast
from typing import List
from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
from backend.utils.file_writer import load_python_files

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="TesterAgent", role="Functionality Validator")

    @track_progress_step("TesterAgent", "Tester Agent is executing")
    def execute(self, task_list: List[str]) -> dict:
        """
        task_list is not used currently; future-proofing for test-specific instructions
        Returns: Dict with test_results (list of syntax status messages)
        """
        test_results = []
        files_to_test = load_python_files("output_projects")

        for file_path, content in files_to_test.items():
            try:
                ast.parse(content)
                test_results.append(f"{file_path}: ✅ Syntax OK")
            except SyntaxError as e:
                test_results.append(f"{file_path}: ❌ Syntax Error - {e} (<unknown>, line {e.lineno})")

        self.remember("test_results", test_results)
        return {"test_results": test_results}
