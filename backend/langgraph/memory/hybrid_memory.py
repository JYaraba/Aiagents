# File: backend/langgraph/memory/hybrid_memory.py

from backend.langgraph.memory.faiss_memory import FAISSMemory
from backend.langgraph.memory.json_memory import JSONMemory
from pathlib import Path

# Base folder to store memory files
MEMORY_DIR = Path("memory_store")
MEMORY_DIR.mkdir(exist_ok=True)

# Set file paths
FAISS_INDEX_PATH = MEMORY_DIR / "faiss.index"
FAISS_META_PATH = MEMORY_DIR / "faiss_metadata.json"
JSON_MEMORY_PATH = MEMORY_DIR / "json_memory.json"  # Added file path for JSONMemory

class HybridMemoryManager:
    def __init__(self):
        self.faiss_memory = FAISSMemory(
            index_path=str(FAISS_INDEX_PATH),
            metadata_path=str(FAISS_META_PATH)
        )
        self.json_memory = JSONMemory(file_path=str(JSON_MEMORY_PATH))  # Pass file_path

    def save(self, agent_name, data):
        self.json_memory.save(agent_name, data)
        self.faiss_memory.save(agent_name, data)

    def recall(self, agent_name, query):
        json_result = self.json_memory.recall(agent_name, query)
        faiss_result = self.faiss_memory.recall(agent_name, query)
        return {
            "json": json_result,
            "faiss": faiss_result
        }

    def clear(self):
        self.json_memory.clear()
        self.faiss_memory.clear()

# ✅ Exported instance for use across system
memory_manager = HybridMemoryManager()