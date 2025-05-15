from datetime import datetime

def log_progress_step(agent_name: str, message: str, data: any = None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = f"[Progress] {timestamp}: {agent_name}: {message}"
    if data:
        output += f" | Data: {data}"
    print(output)
