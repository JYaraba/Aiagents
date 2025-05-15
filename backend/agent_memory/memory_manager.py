import os
from pathlib import Path
from backend.langgraph.memory.faiss_memory import load_faiss_memory, save_faiss_memory
from backend.langgraph.memory.json_memory import load_json_memory, save_json_memory

class MemoryManager:
    def __init__(self, project_id: str, root_folder: str = "output_projects"):
        self.project_id = project_id
        self.root_folder = Path(root_folder)
        self.project_path = self.root_folder / project_id
        self.memory_path = self.project_path / "memory"
        self.vector_store_path = self.memory_path / "vector_store"
        self.json_memory_path = self.memory_path / "memory.json"

        self.memory_path.mkdir(parents=True, exist_ok=True)
        self.vector_store_path.mkdir(parents=True, exist_ok=True)

    def load_memory(self):
        """Load both FAISS (vector) and JSON (sequential) memory."""
        memory = {}
        if self.vector_store_path.exists():
            memory["vector"] = load_faiss_memory(self.vector_store_path)
        else:
            memory["vector"] = None

        if self.json_memory_path.exists():
            try:
                memory["json"] = load_json_memory(self.json_memory_path)
            except Exception as e:
                print(f"[MemoryManager] Warning loading JSON memory: {e}")
                memory["json"] = []
        else:
            memory["json"] = []

        return memory

    def save_memory(self, memory):
        """Save both FAISS and JSON memory."""
        if memory.get("vector"):
            save_faiss_memory(memory["vector"], self.vector_store_path)

        if memory.get("json") is not None:
            save_json_memory(memory["json"], self.json_memory_path)
