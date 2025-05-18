# aiagents/utils/progress_logger.py

def log_step(agent_name: str, step_desc: str):
    print(f"[{agent_name}] ➤ {step_desc}")
