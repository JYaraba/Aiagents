from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step
from aiagents.utils.file_parser import find_python_files, extract_code_blocks
from aiagents.utils.file_writer import write_python_file
import ast


class BugFixerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BugFixerAgent", role="Bug Identification and Fixing")

    @log_progress_step("BugFixerAgent", "Scanning and fixing Python bugs")
    def execute(self, prompt: str) -> dict:
        """
        Scans all generated Python files, detects syntax issues, and fixes minor bugs.
        Returns the list of files fixed or reviewed.
        """
        results = []
        files_to_check = find_python_files("output")

        for file_path, code in files_to_check.items():
            try:
                ast.parse(code)
                results.append(f"{file_path}: ✅ No syntax errors found.")
            except SyntaxError as e:
                results.append(f"{file_path}: ❌ Syntax Error - {e}")
                fixed_code = self._attempt_fix(code, e)
                write_python_file(file_path, fixed_code)
                results.append(f"{file_path}: 🛠️ Attempted fix applied.")

        self.remember("bugfix_summary", results)
        return {"bugfix_summary": results}

    def _attempt_fix(self, code: str, error: SyntaxError) -> str:
        """
        Very basic fix simulation (e.g., appends 'pass' to empty class/function).
        More intelligent logic can be plugged in with AI model.
        """
        lines = code.split('\n')
        if error.lineno is not None and 0 < error.lineno <= len(lines):
            lines.insert(error.lineno, "    pass  # Auto-fix added")
        return "\n".join(lines)
