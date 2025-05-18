from aiagents.agents.architect_agent import ArchitectAgent
from aiagents.agents.planner_agent import PlannerAgent
from aiagents.agents.prompt_engineer_agent import PromptEngineerAgent
from aiagents.agents.frontend_developer_agent import FrontendDeveloperAgent
from aiagents.agents.backend_developer_agent import BackendDeveloperAgent
from aiagents.agents.fullstack_integrator_agent import FullStackIntegratorAgent
from aiagents.agents.uiux_designer_agent import UIUXDesignerAgent
from aiagents.agents.bug_fixer_agent import BugFixerAgent
from aiagents.agents.packager_agent import PackagerAgent
from aiagents.agents.tester_agent import TesterAgent
from aiagents.agents.devops_agent import DevOpsAgent
from aiagents.agents.nodejs_developer_agent import NodeJsDeveloperAgent
from aiagents.agents.python_developer_agent import PythonDeveloperAgent
from aiagents.agents.memory_agent import MemoryAgent
from aiagents.agents.manager_agent import ManagerAgent

# Dictionary to register agent handlers
AGENT_REGISTRY = {
    "ArchitectAgent": ArchitectAgent(),
    "PlannerAgent": PlannerAgent(),
    "PromptEngineerAgent": PromptEngineerAgent(),
    "FrontendDeveloperAgent": FrontendDeveloperAgent(),
    "BackendDeveloperAgent": BackendDeveloperAgent(),
    "FullStackIntegratorAgent": FullStackIntegratorAgent(),
    "UIUXDesignerAgent": UIUXDesignerAgent(),
    "BugFixerAgent": BugFixerAgent(),
    "PackagerAgent": PackagerAgent(),
    "TesterAgent": TesterAgent(),
    "DevOpsAgent": DevOpsAgent(),
    "NodeJsDeveloperAgent": NodeJsDeveloperAgent(),
    "PythonDeveloperAgent": PythonDeveloperAgent(),
    "MemoryAgent": MemoryAgent(),
    "ManagerAgent": ManagerAgent()
}

def route_task(agent_name: str, task_input: str) -> str:
    """
    Routes the task to the appropriate agent based on the agent_name.

    Parameters:
        agent_name (str): The agent responsible for executing the task.
        task_input (str): The prompt or task context for the agent.

    Returns:
        str: The output of the agent after executing the task.
    """
    agent = AGENT_REGISTRY.get(agent_name)
    if not agent:
        raise ValueError(f"Agent '{agent_name}' not found in the registry.")

    return agent.execute(task_input)
