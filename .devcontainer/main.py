from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from aiagents.agents.agent_coordinator import AgentCoordinator

# Initialize FastAPI app
app = FastAPI()

# Instantiate your agent coordinator
coordinator = AgentCoordinator()

# Request schema
class PromptRequest(BaseModel):
    prompt: str

# Health check endpoint
@app.get("/")
def read_root():
    return {"status": "Aiagents backend is running!"}

# Dry run execution endpoint
@app.post("/run-dry")
async def run_dry(request: PromptRequest):
    try:
        result = coordinator.run(prompt=request.prompt)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
