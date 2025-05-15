from backend.agents.planner_agent_runner import run_planner_agent
from backend.agents.developer_agent_runner import run_developer_agent
from backend.utils.preview_renderer import render_preview
from backend.utils.file_writer import write_code_to_project_structure, zip_output_folder, generate_executable_if_possible
from backend.utils.progress_tracker import log_progress_step

def plan_and_build(prompt: str):
    log_progress_step("PlannerAgent", "Starting planning")
    steps = run_planner_agent(prompt)

    log_progress_step("DeveloperAgent", "Executing development tasks")
    code_files = run_developer_agent(steps)

    output_path = "output_projects"
    write_code_to_project_structure(code_files, output_path)

    log_progress_step("DeveloperAgent", "Rendering preview")
    preview_html = render_preview(code_files, output_path)

    log_progress_step("DeveloperAgent", "Packaging build")
    generate_executable_if_possible(output_path)
    zip_output_folder(output_path, "output.zip")

    return {
        "message": "Code generated successfully",
        "preview": preview_html
    }
