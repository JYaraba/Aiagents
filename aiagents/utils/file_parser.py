# aiagents/utils/file_parser.py

import os
from typing import List

def find_python_files(directory: str) -> List[str]:
    """Recursively find all Python files in a directory."""
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files

def extract_code_blocks(file_path: str) -> List[str]:
    """Extract blocks of code (functions/classes) from a Python file."""
    with open(file_path, "r") as f:
        lines = f.readlines()

    code_blocks = []
    block = []
    for line in lines:
        if line.strip().startswith(("def ", "class ")):
            if block:
                code_blocks.append("".join(block))
                block = []
        block.append(line)

    if block:
        code_blocks.append("".join(block))

    return code_blocks
