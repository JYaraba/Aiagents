import os
from backend.langgraph.memory.json_memory import JSONMemory
from backend.langgraph.memory.faiss_memory import FAISSMemory

class HybridMemoryManager:
    def __init__(
        self,
        faiss_index_path="data/faiss_index.index",
        faiss_metadata_path="data/faiss_metadata.json",
        json_file_path="data/memory.json"
    ):
        os.makedirs("data", exist_ok=True)
        self.faiss_memory = FAISSMemory(index_path=faiss_index_path, metadata_path=faiss_metadata_path)
        self.json_memory = JSONMemory(file_path=json_file_path)

    def store(self, key: str, value: str):
        self.json_memory.store(key, value)
        self.faiss_memory.store(key, value)

    def recall(self, key: str) -> str | None:
        # First try semantic recall
        sem = self.faiss_memory.recall(key)
        if sem:
            return sem
        return self.json_memory.recall(key)
