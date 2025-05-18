from crewai import Crew
from aiagents.agents.architect_agent import ArchitectAgent
from aiagents.agents.planner_agent import PlannerAgent
from aiagents.agents.prompt_engineer_agent import PromptEngineerAgent
from aiagents.agents.frontend_developer_agent import FrontendDeveloperAgent
from aiagents.agents.backend_developer_agent import BackendDeveloperAgent
from aiagents.agents.nodejs_developer_agent import NodeJsDeveloperAgent
from aiagents.agents.python_developer_agent import PythonDeveloperAgent
from aiagents.agents.uiux_designer_agent import UIUXDesignerAgent
from aiagents.agents.fullstack_integrator_agent import FullStackIntegratorAgent
from aiagents.agents.tester_agent import TesterAgent
from aiagents.agents.bug_fixer_agent import BugFixerAgent
from aiagents.agents.packager_agent import PackagerAgent
from aiagents.agents.memory_agent import MemoryAgent
from aiagents.agents.devops_agent import DevOpsAgent
from aiagents.agents.manager_agent import ManagerAgent

def create_aiagents_crew():
    """
    Initializes and returns the full Crew instance with all configured agents.
    """
    return Crew(
        agents=[
            ArchitectAgent(),
            PlannerAgent(),
            PromptEngineerAgent(),
            UIUXDesignerAgent(),
            FrontendDeveloperAgent(),
            BackendDeveloperAgent(),
            NodeJsDeveloperAgent(),
            PythonDeveloperAgent(),
            FullStackIntegratorAgent(),
            TesterAgent(),
            BugFixerAgent(),
            PackagerAgent(),
            MemoryAgent(),
            DevOpsAgent(),
            ManagerAgent(),
        ],
        shared_instructions="Collaborate to analyze the prompt, plan development, generate the app code, test it, fix bugs, and package the result. Work as a coordinated software team."
    )
