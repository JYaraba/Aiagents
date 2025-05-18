from functools import wraps

def log_progress_step(agent_name, step_description):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{agent_name}] ➤ {step_description}")
            return func(*args, **kwargs)
        return wrapper  # ✅ This line is critical
    return decorator  # ✅ And this too
