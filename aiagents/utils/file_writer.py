# aiagents/utils/file_writer.py

import os

def write_react_file(component_name: str, content: str, output_dir: str = "output_projects/react-app/src/components"):
    """
    Write a React component file to the specified directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{component_name}.jsx")

    with open(filename, "w") as f:
        f.write(content)

    return filename


def write_code_file(file_path: str, content: str):
    """
    Write backend or general code to the specified file path.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)


def write_json_file(file_path: str, data: dict):
    """
    Write JSON data to a file.
    """
    import json
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def write_python_file(file_path: str, content: str):
    """
    Write Python code to a file, ensuring proper folder structure.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)
