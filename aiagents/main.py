import sys
import os

# Absolute path to the project root
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from fastapi import FastAPI
from pydantic import BaseModel
from aiagents.agents.agent_coordinator import AgentCoordinator  # ✅ Now this will work

app = FastAPI()
coordinator = AgentCoordinator()

class BuildRequest(BaseModel):
    app_prompt: str

@app.post("/build")
def build_app(request: BuildRequest):
    return coordinator.run(request.app_prompt)
