from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_logger import log_step
import re
import os

class BugFixerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BugFixerAgent",
            role="Code Repair Specialist",
            goal="Fix code issues identified by the TesterAgent, such as syntax errors or missing elements.",
        )

    @log_step("BugFixerAgent", "Analyzing test output for fixes")
    def execute(self, context: dict) -> dict:
        test_results = context.get("test_results", [])
        fixes_applied = []

        for result in test_results:
            if "Syntax Error" in result:
                match = re.match(r"(.*?): ❌ Syntax Error - .*?line (\d+)", result)
                if match:
                    file_path, line_number = match.groups()
                    line_number = int(line_number)

                    if os.path.exists(file_path):
                        with open(file_path, "r", encoding="utf-8") as f:
                            lines = f.readlines()

                        if 0 <= line_number - 1 < len(lines):
                            original = lines[line_number - 1]
                            lines[line_number - 1] = f"# Auto-removed due to syntax error: {original}"

                            with open(file_path, "w", encoding="utf-8") as f:
                                f.writelines(lines)

                            fixes_applied.append(f"Auto-commented line {line_number} in {file_path}")

        self.remember("fixes_applied", fixes_applied)
        return {"fixes_applied": fixes_applied}
