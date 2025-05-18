from aiagents.base.base_agent import BaseAgent
from aiagents.utils.logging_utils import log_agent_step
from aiagents.utils.file_writer import write_code_to_file
from aiagents.utils.llm_connector import call_llm

class NodeJsDeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="NodeJsDeveloperAgent", role="Backend Developer (Node.js)")

    @log_agent_step("NodeJsDeveloperAgent", "Generating backend code in Node.js")
    def execute(self, task: dict) -> dict:
        """
        Generates Node.js backend code based on task input and writes it to appropriate files.
        """
        try:
            prompt = task.get("prompt", "")
            files_to_generate = task.get("files", {})
            written_files = []

            for file_path, description in files_to_generate.items():
                full_prompt = f"{prompt}\n\nGenerate Node.js backend code for: {description}"
                code = call_llm(full_prompt)
                write_code_to_file(file_path, code)
                written_files.append(file_path)

            return {"status": "success", "files_created": written_files}

        except Exception as e:
            return {"status": "error", "message": str(e)}
