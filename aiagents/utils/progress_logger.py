# aiagents/utils/progress_logger.py

import datetime
import os
from functools import wraps


def log_progress_step(agent_name: str, message: str):
    """
    Decorator to log the start and end of a function execution with a custom message.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] [{agent_name}] {message}"

            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, f"{agent_name.lower()}_log.txt")

            with open(log_file, "a") as f:
                f.write(log_message + "\n")

            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
