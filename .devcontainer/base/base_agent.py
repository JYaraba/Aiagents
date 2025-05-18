# aiagents/base/base_agent.py

from abc import ABC, abstractmethod
from crewai import Agent
from typing import Optional

class BaseAgent(ABC):
    def __init__(self, name: str, role: str, goal: str, backstory: Optional[str] = None, tools: Optional[list] = None):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory or "An intelligent and proactive AI agent."
        self.tools = tools or []
        self.agent = self._initialize_agent()

    def _initialize_agent(self):
        return Agent(
            name=self.name,
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            tools=self.tools,
            verbose=True
        )

    @abstractmethod
    def run(self, input_data: str):
        pass
