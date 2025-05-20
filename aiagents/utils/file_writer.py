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
def write_file(file_path: str, content: str):
    """
    Generic file writer for any type of content (scripts, Dockerfiles, configs, etc.)
    """
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)
def write_preview_file(file_path: str, content: str):
    """
    Write the given content to a preview file. This is typically used to display code to the frontend.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        raise RuntimeError(f"Failed to write preview file at {file_path}: {e}")

def write_output_file(relative_path: str, content: str):
    """
    Write a string to a file under /output directory, creating directories as needed.
    """
    output_base = os.path.join(os.getcwd(), "output")
    full_path = os.path.join(output_base, relative_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)