import os
import faiss
import pickle
import numpy as np
from pathlib import Path
from typing import List
from sentence_transformers import SentenceTransformer

class FAISSMemory:
    def __init__(self, index_path: str, metadata_path: str):
        self.index_path = Path(index_path)
        self.metadata_path = Path(metadata_path)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        if self.index_path.exists() and self.metadata_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            with open(self.metadata_path, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)  # Vector size for MiniLM
            self.metadata = []

    def save(self):
        faiss.write_index(self.index, str(self.index_path))
        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def add(self, text: str, metadata: dict):
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding).astype("float32"))
        self.metadata.append(metadata)
        self.save()

    def search(self, query: str, top_k: int = 5) -> List[dict]:
        embedding = self.model.encode([query])
        D, I = self.index.search(np.array(embedding).astype("float32"), top_k)
        return [self.metadata[i] for i in I[0] if i < len(self.metadata)]
