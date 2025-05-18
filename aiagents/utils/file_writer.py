import os
from typing import Dict


def ensure_directory_exists(file_path: str) -> None:
    """Ensure the directory for the given file path exists."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


def write_text_file(file_path: str, content: str) -> None:
    """Write text content to a file, overwriting if it exists."""
    ensure_directory_exists(file_path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def write_multiple_files(file_map: Dict[str, str]) -> None:
    """
    Write multiple files from a dictionary of {path: content}.
    """
    for path, content in file_map.items():
        try:
            write_text_file(path, content)
        except Exception as e:
            print(f"Failed to write {path}: {e}")


def append_to_file(file_path: str, content: str) -> None:
    """Append content to an existing file."""
    ensure_directory_exists(file_path)
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)


def file_exists(file_path: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(file_path)
