# backend/agents/memory_agent.py

import json
import os
from .base_agent import BaseAgent
from backend.utils.progress_tracker import track_progress_step

class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="MemoryAgent", role="Long-Term Memory Keeper")
        self.memory_path = "output/memory.json"
        os.makedirs("output", exist_ok=True)

        # Load existing memory or initialize empty
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    @track_progress_step("MemoryAgent", "Saving new memory entry")
    def remember(self, key: str, value):
        self.memory[key] = value
        with open(self.memory_path, "w") as f:
            json.dump(self.memory, f, indent=2)

    @track_progress_step("MemoryAgent", "Retrieving memory entry")
    def recall(self, key: str):
        return self.memory.get(key, None)

    @track_progress_step("MemoryAgent", "Listing all memory keys")
    def list_keys(self):
        return list(self.memory.keys())
