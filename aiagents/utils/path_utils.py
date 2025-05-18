# aiagents/utils/path_utils.py

import os

def resolve_output_path(base_dir: str, *paths: str) -> str:
    """
    Resolves and creates an output path under the given base directory.
    Example:
        resolve_output_path("output_projects/backend", "services", "auth", "auth_service.py")
        -> output_projects/backend/services/auth/auth_service.py
    """
    full_path = os.path.join(base_dir, *paths)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path
