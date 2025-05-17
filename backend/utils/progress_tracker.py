import datetime
import functools
import inspect
from functools import wraps
from datetime import datetime
from typing import Any, Optional

def log_progress_step(agent_name: str, message: str, extra: Optional[Any] = None):
    print(f"[{agent_name}] {message}")
    if extra is not None:
        print(f"[{agent_name} DATA] {extra}")

def track_progress_step(agent: str, progress: str):
    """
    Decorator to automatically log before and after executing a function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_progress_step(agent, progress)
            result = func(*args, **kwargs)
            log_progress_step(agent, f"{progress} - Completed")
            return result
        return wrapper
    return decorator


