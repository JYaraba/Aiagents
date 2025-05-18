import json
import os

class BaseAgent:
    def __init__(self, name: str, role: str, goal: str = ""):
        self.name = name
        self.role = role
        self.goal = goal
        self.memory_file = f"aiagents/memory/{self.name}_memory.json"
        self._ensure_memory_file()

    def _ensure_memory_file(self):
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump({}, f)

    def remember(self, key: str, value):
        memory = self._load_memory()
        memory[key] = value
        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=2)

    def recall(self, key: str):
        memory = self._load_memory()
        return memory.get(key, None)

    def _load_memory(self):
        with open(self.memory_file, "r") as f:
            return json.load(f)
