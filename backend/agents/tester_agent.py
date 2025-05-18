from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_loader import load_project_files
from aiagents.utils.progress_logger import log_step
import ast


class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TesterAgent",
            role="QA Tester",
            goal="Ensure all generated files are free from syntax errors and basic issues before packaging."
        )

    @log_step("TesterAgent is executing test pass")
    def execute(self, inputs: dict) -> dict:
        # Load all output project files
        file_map = load_project_files("output")

        test_results = []
        issues_detected = False

        for file_path, content in file_map.items():
            if file_path.endswith(".js") or file_path.endswith(".json") or file_path.endswith(".html"):
                # For non-Python files, we can do lightweight lint checks in future
                continue

            if file_path.endswith(".py"):
                try:
                    ast.parse(content)
                    test_results.append(f"{file_path}: ✅ Syntax OK")
                except SyntaxError as e:
                    issues_detected = True
                    test_results.append(f"{file_path}: ❌ Syntax Error - {e}")

        output = {
            "test_results": test_results,
            "issues_found": issues_detected
        }

        self.remember("test_results", test_results)
        return output
