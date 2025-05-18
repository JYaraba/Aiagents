import os
import shutil
from typing import List


def create_folder(path: str) -> None:
    """Create a folder if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def clear_folder(path: str) -> None:
    """Delete and recreate a folder to ensure it's clean."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def list_all_files(folder: str) -> List[str]:
    """Recursively list all files in the given folder."""
    file_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            file_list.append(full_path)
    return file_list


def copy_folder_contents(source: str, destination: str) -> None:
    """Copy the entire contents of one folder to another."""
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source folder not found: {source}")

    create_folder(destination)

    for item in os.listdir(source):
        s_item = os.path.join(source, item)
        d_item = os.path.join(destination, item)
        if os.path.isdir(s_item):
            shutil.copytree(s_item, d_item, dirs_exist_ok=True)
        else:
            shutil.copy2(s_item, d_item)
