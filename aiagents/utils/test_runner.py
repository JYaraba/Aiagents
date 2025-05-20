import ast
import os
import subprocess
from typing import List, Tuple


def find_python_files(root_path: str) -> List[str]:
    """
    Recursively find all .py files in the given root directory.
    """
    python_files = []
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(dirpath, filename)
                python_files.append(full_path)
    return python_files


def check_syntax(file_path: str) -> Tuple[str, bool, str]:
    """
    Parse the given Python file and return whether it contains valid syntax.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
            ast.parse(source)
        return (file_path, True, "")
    except SyntaxError as e:
        return (file_path, False, str(e))
    except Exception as e:
        return (file_path, False, f"Unexpected error: {e}")


def run_basic_syntax_tests(directory: str) -> List[str]:
    """
    Run syntax checks on all Python files in the specified directory.
    Returns a list of results.
    """
    results = []
    python_files = find_python_files(directory)
    for file_path in python_files:
        path, is_valid, error = check_syntax(file_path)
        if is_valid:
            results.append(f"{path}: ✅ Syntax OK")
        else:
            results.append(f"{path}: ❌ Syntax Error - {error}")
    return results

def run_code_tests(output_dir="output_projects"):
    """
    Run code syntax checks or test scripts for all files in the output directory.
    This is a placeholder function that runs `python -m py_compile` on each file.
    """
    results = []
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    subprocess.check_output(["python3", "-m", "py_compile", file_path], stderr=subprocess.STDOUT)
                    results.append(f"{file_path}: ✅ Syntax OK")
                except subprocess.CalledProcessError as e:
                    results.append(f"{file_path}: ❌ Syntax Error - {e.output.decode().strip()}")
    return results