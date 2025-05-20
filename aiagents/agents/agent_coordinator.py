# File: aiagents/agents/agent_coordinator.py

from aiagents.agents.architect_agent import ArchitectAgent
from aiagents.agents.planner_agent import PlannerAgent
from aiagents.agents.manager_agent import ManagerAgent
from aiagents.agents.devops_agent import DevOpsAgent
from aiagents.agents.bug_fixer_agent import BugFixerAgent
from aiagents.agents.tester_agent import TesterAgent
from aiagents.agents.prompt_engineer_agent import PromptEngineerAgent
from aiagents.agents.frontend_developer_agent import FrontendDeveloperAgent
from aiagents.agents.backend_developer_agent import BackendDeveloperAgent
from aiagents.agents.nodejs_developer_agent import NodeJsDeveloperAgent
from aiagents.agents.java_developer_agent import JavaDeveloperAgent
from aiagents.agents.python_developer_agent import PythonDeveloperAgent
from aiagents.agents.uiux_designer_agent import UIUXDesignerAgent
from aiagents.agents.fullstack_integrator_agent import FullStackIntegratorAgent
from aiagents.agents.memory_agent import MemoryAgent
from aiagents.agents.packager_agent import PackagerAgent

class AgentCoordinator:
    def __init__(self):
        self.architect = ArchitectAgent()
        self.planner = PlannerAgent()
        self.manager = ManagerAgent()
        self.devops = DevOpsAgent()
        self.bug_fixer = BugFixerAgent()
        self.tester = TesterAgent()
        self.prompt_engineer = PromptEngineerAgent()
        self.frontend = FrontendDeveloperAgent()
        self.backend = BackendDeveloperAgent()
        self.nodejs = NodeJsDeveloperAgent()
        self.java = JavaDeveloperAgent()
        self.python = PythonDeveloperAgent()
        self.uiux = UIUXDesignerAgent()
        self.fullstack = FullStackIntegratorAgent()
        self.memory = MemoryAgent()
        self.packager = PackagerAgent()

    def plan_and_build(self, app_prompt: str) -> dict:
        """
        Accepts a string prompt and coordinates agents to build the application.
        """
        print("🚀 Starting plan_and_build with prompt:", app_prompt)

        # Step 1: Use the planner agent
        tasks = self.planner.execute(app_prompt)

        # Step 2: Store in memory
        self.memory.store("tasks", tasks)

        # Step 3: Run design
        ui_plan = self.uiux.execute(tasks)
        arch_plan = self.architect.execute(tasks)

        # Step 4: Use developers
        frontend_result = self.frontend.execute(ui_plan)
        backend_result = self.backend.execute(arch_plan)

        # Step 5: Integrate
        integration_result = self.fullstack.execute([frontend_result, backend_result])

        # Step 6: Test
        test_results = self.tester.execute([frontend_result, backend_result])

        # Step 7: Fix bugs if needed
        fix_report = self.bug_fixer.execute(test_results)

        # Step 8: Package app
        package = self.packager.execute(integration_result)

        return {
            "tasks": tasks,
            "ui_plan": ui_plan,
            "arch_plan": arch_plan,
            "frontend": frontend_result,
            "backend": backend_result,
            "integration": integration_result,
            "test_results": test_results,
            "fix_report": fix_report,
            "package": package
        }
