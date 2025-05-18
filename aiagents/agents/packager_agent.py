import os
import shutil
from zipfile import ZipFile

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_logger import log_step


class PackagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PackagerAgent",
            role="Application Packager",
            goal="Bundle the generated application files into a downloadable zip archive."
        )

    @log_step("PackagerAgent", "Packaging build output")
    def execute(self, context: dict) -> dict:
        output_folder = context.get("output_folder", "output_projects")
        package_output_path = "output/package.zip"

        if not os.path.exists("output"):
            os.makedirs("output")

        # Clean previous archive if any
        if os.path.exists(package_output_path):
            os.remove(package_output_path)

        # Zip the directory recursively
        with ZipFile(package_output_path, 'w') as zipf:
            for root, _, files in os.walk(output_folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, output_folder)
                    zipf.write(full_path, arcname=relative_path)

        self.remember("package_path", package_output_path)

        return {
            "package_path": package_output_path,
            "message": f"Project packaged successfully at {package_output_path}"
        }
