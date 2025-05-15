def detect_stack(code_files: dict[str, str]) -> str:
    for file_name in code_files:
        if "flask" in code_files[file_name].lower():
            return "Flask"
        elif "react" in code_files[file_name].lower():
            return "React"
    return "Unknown"
