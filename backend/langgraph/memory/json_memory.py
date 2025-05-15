import json
from pathlib import Path
from typing import Any, List

class JSONMemory:
    def __init__(self, file_path: str):
        self.path = Path(file_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text(json.dumps({}))

    def load(self) -> dict:
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save(self, memory: dict):
        try:
            with open(self.path, "w") as f:
                json.dump(memory, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save memory to {self.path}: {e}")

    def append(self, key: str, value: Any):
        data = self.load()
        if key not in data:
            data[key] = []
        data[key].append(value)
        self.save(data)

    def get(self, key: str) -> List[Any]:
        data = self.load()
        return data.get(key, [])