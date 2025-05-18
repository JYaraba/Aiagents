# aiagents/utils/memory_store.py

# aiagents/utils/memory_store.py

class MemoryStore:
    def __init__(self):
        self.memory = {}

    def store(self, key: str, value: str):
        self.memory[key] = value

    def retrieve(self, key: str):
        return self.memory.get(key, "")

    def delete(self, key: str):
        if key in self.memory:
            del self.memory[key]

    def list_keys(self):
        return list(self.memory.keys())

