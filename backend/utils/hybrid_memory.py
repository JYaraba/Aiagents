import json
import os
from typing import List, Dict, Any
from pathlib import Path
from uuid import uuid4
import faiss
import numpy as np
from openai import OpenAI
from backend.config import settings

MEMORY_DIR = Path("backend/memory_store")
MEMORY_DIR.mkdir(parents=True, exist_ok=True)

class HybridMemory:
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.json_path = MEMORY_DIR / f"{agent_name}_memory.json"
        self.index_path = MEMORY_DIR / f"{agent_name}_index.faiss"
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.embeddings_model = "text-embedding-ada-002"

        self.memory_data = self._load_json_memory()
        self.index, self.id_map = self._load_or_initialize_index()

    def _load_json_memory(self) -> List[Dict[str, Any]]:
        if self.json_path.exists():
            with open(self.json_path, "r") as f:
                return json.load(f)
        return []

    def _save_json_memory(self):
        with open(self.json_path, "w") as f:
            json.dump(self.memory_data, f, indent=2)

    def _load_or_initialize_index(self):
        dim = 1536  # For text-embedding-ada-002
        if self.index_path.exists() and (MEMORY_DIR / f"{self.agent_name}_id_map.json").exists():
            index = faiss.read_index(str(self.index_path))
            with open(MEMORY_DIR / f"{self.agent_name}_id_map.json", "r") as f:
                id_map = json.load(f)
        else:
            index = faiss.IndexFlatL2(dim)
            id_map = {}
        return index, id_map

    def _save_index(self):
        faiss.write_index(self.index, str(self.index_path))
        with open(MEMORY_DIR / f"{self.agent_name}_id_map.json", "w") as f:
            json.dump(self.id_map, f)

    def _embed(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model=self.embeddings_model,
            input=[text]
        )
        return response.data[0].embedding

    def add_memory(self, text: str, metadata: Dict[str, Any]):
        embedding = self._embed(text)
        uid = str(uuid4())
        self.index.add(np.array([embedding], dtype=np.float32))
        self.id_map[str(len(self.id_map))] = uid
        self.memory_data.append({"id": uid, "text": text, "metadata": metadata})
        self._save_index()
        self._save_json_memory()

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        if len(self.memory_data) == 0:
            return []

        query_vec = np.array([self._embed(query)], dtype=np.float32)
        _, indices = self.index.search(query_vec, top_k)

        results = []
        for idx in indices[0]:
            if str(idx) in self.id_map:
                uid = self.id_map[str(idx)]
                entry = next((item for item in self.memory_data if item["id"] == uid), None)
                if entry:
                    results.append(entry)
        return results

    def clear_memory(self):
        self.memory_data = []
        self.index = faiss.IndexFlatL2(1536)
        self.id_map = {}
        self._save_index()
        self._save_json_memory()

    def dump(self) -> List[Dict[str, Any]]:
        return self.memory_data

    def load_context_for_prompt(self, current_prompt: str) -> str:
        context_entries = self.search(current_prompt, top_k=3)
        context_texts = [entry["text"] for entry in context_entries]
        return "\n---\n".join(context_texts)

