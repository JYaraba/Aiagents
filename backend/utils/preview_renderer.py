from pathlib import Path

def render_preview(code_files: dict[str, str], output_dir: Path):
    html = "<html><head><title>Generated Code</title></head><body><h1>Code Preview</h1><ul>"
    for file_path, content in code_files.items():
        html += f"<li><h3>{file_path}</h3><pre><code>{content}</code></pre></li>"
    html += "</ul></body></html>"

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(html)
    print(f"[Preview] index.html created in {output_dir}")
    return str(output_dir / "index.html")
