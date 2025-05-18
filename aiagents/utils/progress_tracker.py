import datetime
import functools

def log_progress_step(agent_name: str, step_description: str):
    """
    Decorator to log agent progress in a standardized format.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{start_time}] ▶️ [{agent_name}] START: {step_description}")
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{end_time}] ✅ [{agent_name}] DONE: {step_description}")
            return result
        return wrapper
    return decorator
