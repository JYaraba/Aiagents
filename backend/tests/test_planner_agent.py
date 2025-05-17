import pytest
from agents.planner_agent import PlannerAgent
from backend.config import settings

@pytest.mark.skipif(not settings.OPENAI_API_KEY, reason="No OpenAI key set")
def test_planner_agent_execution():
    agent = PlannerAgent()
    prompt = "Build a simple expense tracking app"
    tasks = agent.execute(prompt)

    assert isinstance(tasks, list)
    assert len(tasks) >= 3
    assert any("UI" in task or "interface" in task.lower() for task in tasks)
