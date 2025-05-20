# aiagents/agents/memory_agent.py

from pydantic import PrivateAttr
from aiagents.base.base_agent import BaseAgent
from aiagents.utils.progress_tracker import log_progress_step


class MemoryAgent(BaseAgent):
    _memory: dict = PrivateAttr(default_factory=dict)

    def __init__(self):
        super().__init__(
            name="MemoryAgent",
            role="Memory Manager",
            goal="Store and retrieve contextual memory from previous tasks across agents.",
            backstory=(
                "You manage the persistent memory system across the agent crew. You help agents recall previous actions, decisions, and task history "
                "to ensure context-aware behavior in ongoing and future tasks."
            )
        )

    @log_progress_step("MemoryAgent", "Storing and retrieving agent memory")
    def execute(self, task_data: dict) -> dict:
        return {
            "status": "executed",
            "agent": "MemoryAgent",
            "details": "Memory operation completed."
        }

    def store(self, key: str, value: any) -> None:
        self._memory[key] = value

    def retrieve(self, key: str) -> any:
        return self._memory.get(key)

    def all_memory(self) -> dict:
        return self._memory
