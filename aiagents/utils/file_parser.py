import os
from typing import Dict


def read_file(file_path: str) -> str:
    """Read a file and return its content."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def read_all_files_in_directory(directory_path: str, extensions: tuple = (".py", ".js", ".html")) -> Dict[str, str]:
    """
    Recursively read all files with given extensions from a directory and return a mapping of file paths to content.
    """
    file_map = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                try:
                    content = read_file(full_path)
                    file_map[full_path] = content
                except Exception as e:
                    print(f"Error reading {full_path}: {e}")
    return file_map
