# backend/agents/packager_agent.py

import os
import zipfile
from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step

class PackagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PackagerAgent", role="Application Packager")

    @track_progress_step("PackagerAgent", "Packaging build output")
    def execute(self, task_list: list[str]) -> dict:
        """
        task_list is unused for now; future: allow packaging config
        Returns: path to zipped package
        """
        output_dir = "output_projects"
        zip_path = "output/package.zip"
        os.makedirs("output", exist_ok=True)

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, output_dir)
                    zipf.write(abs_path, arcname=rel_path)

        self.remember("last_package_path", zip_path)
        return {"zip_path": zip_path}
