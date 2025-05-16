from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step
import os

class TesterAgent(BaseAgent):
    def __init__(self):
        super().__init__("TesterAgent", "Application Tester")

    @track_progress_step("TesterAgent", "Executing tests")
    def execute(self, task_list: list[str]) -> dict:
        test_results = []
        issues = []

        for file in os.listdir("output_projects"):
            if file.endswith(".py"):
                file_path = os.path.join("output_projects", file)
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                        if "def" not in content:
                            issues.append(f"{file} is missing function definitions.")
                        if "import" not in content:
                            issues.append(f"{file} may be missing imports.")
                except Exception as e:
                    issues.append(f"Error reading {file}: {str(e)}")

        result_summary = "All files checked. Issues: " + str(issues if issues else "None.")
        self.remember("last_test_issues", issues)
        return {
            "issues": issues,
            "summary": result_summary
        }
