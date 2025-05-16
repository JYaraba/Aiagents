from pathlib import Path

def render_preview(code_files: dict, output_dir: str) -> str:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    preview_path = output_path / "preview.html"

    # Combine all code into a single HTML-safe block
    all_code = "\n\n".join([f"# File: {name}\n{content}" for name, content in code_files.items()])
    html = f"<html><body><pre>{all_code}</pre></body></html>"

    with open(preview_path, "w") as f:
        f.write(html)

    return str(preview_path)
