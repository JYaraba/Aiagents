import json
import os
from pathlib import Path
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from aiagents.crew.task_router import route_task
from aiagents.agents.agent_coordinator import plan_and_build
from aiagents.agents.memory_agent import MemoryAgent
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
from aiagents.agents.devops_agent import DevOpsAgent
from aiagents.agents.manager_agent import ManagerAgent
from aiagents.crew.task_router import route_task


MEMORY_FOLDER = Path("aiagents/memory/")
VECTOR_STORE_PATH = MEMORY_FOLDER / "vector_index"
JSON_MEMORY_FILE = MEMORY_FOLDER / "memory.json"

class MemoryManager:
    def __init__(self):
        self.json_memory = self._load_json_memory()
        self.vector_store = self._load_vector_store()

    def _load_json_memory(self):
        MEMORY_FOLDER.mkdir(parents=True, exist_ok=True)
        if JSON_MEMORY_FILE.exists():
            with open(JSON_MEMORY_FILE, "r") as f:
                return json.load(f)
        return {}

    def _load_vector_store(self):
        if VECTOR_STORE_PATH.exists():
            return FAISS.load_local(str(VECTOR_STORE_PATH), OpenAIEmbeddings())
        else:
            return FAISS.from_documents([], OpenAIEmbeddings())

    def save_memory(self, agent_name: str, key: str, value: str):
        # Save to JSON
        if agent_name not in self.json_memory:
            self.json_memory[agent_name] = {}
        self.json_memory[agent_name][key] = value
        with open(JSON_MEMORY_FILE, "w") as f:
            json.dump(self.json_memory, f, indent=2)

        # Save to FAISS
        doc = Document(page_content=value, metadata={"agent": agent_name, "key": key})
        self.vector_store.add_documents([doc])
        self.vector_store.save_local(str(VECTOR_STORE_PATH))

    def retrieve_json_memory(self, agent_name: str, key: str) -> str:
        return self.json_memory.get(agent_name, {}).get(key, "")

    def semantic_search(self, query: str, k: int = 3):
        results = self.vector_store.similarity_search(query, k=k)
        return [res.page_content for res in results]
