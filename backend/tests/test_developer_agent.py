import pytest
from agents.developer_agent import DeveloperAgent
from backend.config import settings

@pytest.mark.skipif(not settings.OPENAI_API_KEY, reason="No OpenAI key set")
def test_developer_agent_execution():
    agent = DeveloperAgent()
    prompt = "Write a Python function that adds two numbers"
    result = agent.execute(prompt)
    
    assert "def" in result.lower()
    assert "add" in result.lower()
