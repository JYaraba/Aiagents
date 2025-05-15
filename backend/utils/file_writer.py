import os
from pathlib import Path
import zipfile

def write_code_to_project_structure(code_files: dict[str, str], output_path: Path) -> None:
    for file_path, code in code_files.items():
        full_path = output_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(code)
    print(f"[Writer] Code written to: {output_path}")

def generate_executable_if_possible(output_path: Path):
    main_file = output_path / "main.py"
    if main_file.exists():
        print("[Executable Generator] Found main.py. Skipping actual .exe generation (not implemented).")
    else:
        print("[Executable Generator] 'main.py' not found. Skipping .exe generation.")

def zip_output_folder(output_path: Path, zip_path: Path = Path("output.zip")):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_path):
            for file in files:
                full_path = Path(root) / file
                relative_path = full_path.relative_to(output_path)
                zipf.write(full_path, arcname=relative_path)
    print(f"[Zipper] Created zip at: {zip_path}")
