from pydantic import BaseModel

class BaseAgent(BaseModel):
    name: str
    role: str
    goal: str
    backstory: str

    def remember(self, key: str, value):
        print(f"[Memory Placeholder] {self.name} remembers {key} = {value}")
