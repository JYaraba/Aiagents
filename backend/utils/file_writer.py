from pathlib import Path
import zipfile
import os


def write_code_to_project_structure(files: dict, output_path: str):
    """
    Writes a dictionary of {filename: code} to a structured folder under output_path.
    """
    output_path = Path(output_path)  # ✅ Ensure it's a Path object

    output_path.mkdir(parents=True, exist_ok=True)

    for file_path, code in files.items():
        full_path = output_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w") as f:
            f.write(code)

def zip_output_folder(source_dir: str, zip_path: str):
    """
    Zips the contents of source_dir into zip_path.
    """
    source_dir = Path(source_dir)  # ✅ Ensure it's a Path object
    zip_path = Path(zip_path)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(source_dir))

def generate_executable_if_possible(main_py_path: str):
    # Placeholder logic - customize this later
    if Path(main_py_path).exists():
        print("[Executable Generator] 'main.py' found, preparing for packaging...")
    else:
        print("[Executable Generator] 'main.py' not found. Skipping .exe generation.")

def load_python_files(folder_path: str) -> dict:
    files = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            with open(os.path.join(folder_path, filename), "r") as f:
                files[filename] = f.read()
    return files