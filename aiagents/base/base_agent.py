from crewai import Agent

class BaseAgent(Agent):
    def __init__(self, name: str, role: str, goal: str):
        super().__init__(
            name=name,
            role=role,
            goal=goal,
        )
