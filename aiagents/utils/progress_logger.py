def log_step(func):
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Completed: {func.__name__}")
        return result
    return wrapper
