from abc import ABC, abstractmethod
from backend.langgraph.memory.hybrid_memory import memory_manager
from dotenv import load_dotenv
import os
load_dotenv() 

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory = memory_manager

    @abstractmethod
    def execute(self, prompt: str):
        pass

    def remember(self, key: str, value: str | list[str]):
        self.memory.store(f"{self.name}_{key}", value)

    def recall(self, key: str):
        return self.memory.recall(f"{self.name}_{key}")
