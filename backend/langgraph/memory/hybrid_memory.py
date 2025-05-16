from backend.langgraph.memory.faiss_memory import FAISSMemory
from backend.langgraph.memory.json_memory import JSONMemory
from pathlib import Path
class HybridMemoryManager:
    def __init__(self):
        base_path = Path("memory_storage")
        base_path.mkdir(exist_ok=True)

        self.faiss_index_path = base_path / "faiss_index"
        self.faiss_metadata_path = base_path / "faiss_metadata.json"
        self.json_memory_path = base_path / "json_memory.json"

        # Initialize FAISS memory with required paths
        self.faiss_memory = FAISSMemory(
            index_path=str(self.faiss_index_path),
            metadata_path=str(self.faiss_metadata_path)
        )

        # Initialize JSON memory with required path
        self.json_memory = JSONMemory(file_path=str(self.json_memory_path))

    def save(self, key, data):
        self.faiss_memory.save(key, data)
        self.json_memory.save(key, data)

    def load(self, key):
        # Prefer FAISS first, fallback to JSON
        faiss_result = self.faiss_memory.load(key)
        if faiss_result:
            return faiss_result
        return self.json_memory.load(key)

# Global instance
memory_manager = HybridMemoryManager()
