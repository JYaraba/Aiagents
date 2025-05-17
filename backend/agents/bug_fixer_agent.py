# backend/agents/bug_fixer_agent.py

import os
import re
from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step

class BugFixerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BugFixerAgent", role="Error Resolver")

    @track_progress_step("BugFixerAgent", "Analyzing test output for fixes")
    def execute(self, test_results: list[str]) -> dict:
        """
        test_results: List of tester output strings (from TesterAgent)
        Returns: Dict of updated files {filename: updated_content}
        """

        fixed_files = {}

        for error in test_results:
            match = re.search(r"^(.*): ❌ Syntax Error - .*\(<unknown>, line (\d+)\)", error)
            if not match:
                continue  # Skip unrecognized formats

            file_path, line_number = match.group(1), int(match.group(2))
            filename = os.path.basename(file_path)
            full_path = os.path.join("output_projects", filename)

            if os.path.exists(full_path):
                with open(full_path, "r") as f:
                    lines = f.readlines()

                if 0 < line_number <= len(lines):
                    print(f"[BugFixerAgent] Auto-removing line {line_number} in {filename}")
                    lines[line_number - 1] = "# [AUTO-FIXED] Removed due to syntax error\n"

                    with open(full_path, "w") as f:
                        f.writelines(lines)

                    fixed_files[filename] = "".join(lines)

        self.remember("fixed_files", fixed_files)
        return fixed_files
