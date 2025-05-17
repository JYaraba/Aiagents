import os
import json
import faiss
import numpy as np
from typing import Any
from sentence_transformers import SentenceTransformer

class FAISSMemory:
    def __init__(self, index_path: str, metadata_path: str):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.keys = []  # ✅ Fix: add missing attribute

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            with open(metadata_path, "r") as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)
            self.metadata = {}

    def save(self, key: str, data: Any):
        try:
            if isinstance(data, list):
                # Flatten list of strings into a single paragraph
                data = "\n".join(map(str, data))
            elif not isinstance(data, str):
                data = str(data)

            embedding = self.model.encode([data])
            self.index.add(np.array(embedding))
            self.keys.append(key)
        except Exception as e:
            print(f"[FAISS Memory Error] Failed to save embedding for {key}: {e}")

    def load(self, key: str):
        for record in self.metadata.values():
            if record["key"] == key:
                return record["data"]
        return None

    def _persist(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f, indent=2)
