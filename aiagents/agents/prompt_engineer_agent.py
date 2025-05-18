# aiagents/agents/prompt_engineer_agent.py

from aiagents.base.base_agent import BaseAgent
from crewai import Task
from typing import List, Dict


class PromptEngineerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="PromptEngineerAgent",
            role="Prompt Engineer",
            goal="Refine and tailor developer tasks into clear, optimized prompts for each agent to execute.",
            backstory=(
                "You are a specialist in translating technical task descriptions into effective prompts. "
                "You help ensure each developer or tester agent gets a clear, contextual instruction they can act on without ambiguity."
            )
        )

    def run(self, task_list: List[Dict]) -> List[Dict]:
        # Input: List of task dicts from PlannerAgent
        # Output: Same list but with optimized prompt
        prompt = (
            f"Refine the following tasks into clear, detailed prompts suitable for AI developer/tester agents. "
            f"Preserve the role and keep each task optimized for action:\n\n{task_list}\n\n"
            f"Return a list of dictionaries with:\n"
            f" - 'agent': role name\n"
            f" - 'prompt': engineered prompt for the agent\n"
        )

        task = Task(
            description=prompt,
            agent=self.agent
        )

        result = task.execute()

        try:
            return eval(result)  # Safe fallback; will replace with json.loads() after dry run validation
        except Exception as e:
            return [{"error": f"Failed to parse prompt engineering output: {str(e)}"}]
