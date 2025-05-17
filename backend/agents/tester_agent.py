from backend.agents.base_agent import BaseAgent
from backend.utils.progress_tracker import log_progress_step
import os

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="TesterAgent", role="Quality Assurance")

    @log_progress_step("TesterAgent", "Tester Agent is executing")
    def execute(self, task_list: list[str]) -> dict:
        issues = []
        test_summary = {}

        # Check if main.py exists
        file_path = "output_projects/main.py"
        if not os.path.exists(file_path):
            issues.append("main.py not found in output_projects folder.")
        else:
            try:
                with open(file_path, "r") as f:
                    code = f.read()
                    compile(code, file_path, "exec")
                    test_summary["main.py"] = "Syntax OK"
            except SyntaxError as e:
                issues.append(f"Syntax error in main.py: {str(e)}")
            except Exception as e:
                issues.append(f"Unexpected error when reading main.py: {str(e)}")

        # Optional: Check for empty preview.html
        preview_path = "output_projects/preview.html"
        if os.path.exists(preview_path):
            with open(preview_path, "r") as f:
                html = f.read().strip()
                if not html:
                    issues.append("preview.html exists but is empty.")
                else:
                    test_summary["preview.html"] = "Found with content"
        else:
            issues.append("preview.html not found.")

        # Save test results to memory
        self.remember("test_results", {"summary": test_summary, "issues": issues})

        return {
            "status": "pass" if not issues else "fail",
            "issues": issues,
            "summary": test_summary
        }
