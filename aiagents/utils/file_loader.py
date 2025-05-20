# aiagents/utils/file_loader.py

import os

def load_project_files(directory="output_projects"):
    """
    Recursively loads all .py files from the specified directory.
    Returns a dict: {file_path: file_content}
    """
    project_files = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    project_files[path] = content
                except Exception as e:
                    project_files[path] = f"Error reading file: {e}"

    return project_files
