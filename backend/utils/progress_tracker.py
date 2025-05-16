import datetime
import functools
import inspect

def log_progress_step(agent: str, step: str, data: object = None):
    """
    Logs progress of a specific agent step with timestamp and optional data.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Progress] {timestamp}: {agent}: {step}", end="")
    if data:
        print(f" | Data: {data}")
    else:
        print("")

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
