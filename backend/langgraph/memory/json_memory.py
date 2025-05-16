import json
import os

class JSONMemory:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def save(self, key: str, data: str):
        with open(self.file_path, 'r') as f:
            memory = json.load(f)

        memory[key] = data

        with open(self.file_path, 'w') as f:
            json.dump(memory, f, indent=2)

    def load(self, key: str):
        if not os.path.exists(self.file_path):
            return None

        with open(self.file_path, 'r') as f:
            memory = json.load(f)

        return memory.get(key)
