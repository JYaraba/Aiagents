from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from backend.schemas.build_request import BuildRequest
from backend.agents.agent_coordinator import plan_and_build
from backend.utils.progress_tracker import log_progress_step

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/build")
def plan_and_generate_code(request: BuildRequest):
    log_progress_step("PlannerAgent", "Starting planning")
    result = plan_and_build(request.prompt)
    return result
