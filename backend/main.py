from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from aiagents.agents.agent_coordinator import AgentCoordinator
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow frontend access (adjust origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class BuildRequest(BaseModel):
    prompt: str

@app.post("/build")
def build_application(request: BuildRequest):
    try:
        coordinator = AgentCoordinator()
        result = coordinator.run(prompt=request.prompt)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
