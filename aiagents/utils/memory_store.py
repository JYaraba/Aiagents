# aiagents/utils/memory_store.py

class MemoryStore:
    """
    A simple in-memory store. This will be extended to use FAISS + JSON later.
    """

    def __init__(self):
        self.memory = {}

    def save(self, key: str, value: str):
        self.memory[key] = value

    def load(self, key: str) -> str:
        return self.memory.get(key, "")

    def get_all(self) -> dict:
        return self.memory
