# aiagents/agents/memory_agent.py

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.memory_store import MemoryStore
from aiagents.utils.progress_logger import log_progress_step


class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="MemoryAgent",
            role="Context Retention and Semantic Memory Handler",
            goal="Store, retrieve, and manage agent memory to improve task continuity and learning."
        )
        self.memory_store = MemoryStore()

    @log_progress_step("MemoryAgent", "Memory Agent is executing")
    def execute(self, context: dict) -> dict:
        """Store relevant context and retrieve past data for assistance."""
        key = context.get("key")
        value = context.get("value")
        action = context.get("action")

        if action == "store":
            self.memory_store.store(key, value)
            return {"status": "stored", "key": key}

        elif action == "retrieve":
            result = self.memory_store.retrieve(key)
            return {"status": "retrieved", "key": key, "value": result}

        elif action == "delete":
            self.memory_store.delete(key)
            return {"status": "deleted", "key": key}

        elif action == "list_keys":
            keys = self.memory_store.list_keys()
            return {"status": "listed", "keys": keys}

        else:
            return {"status": "error", "message": "Unknown action"}
