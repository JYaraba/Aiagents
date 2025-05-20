from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
import logging
from aiagents.agents.agent_coordinator import AgentCoordinator

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    tb_str = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"Unhandled error:\n{tb_str}")
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error", "trace": tb_str},
    )

@app.post("/run-dry")
async def run_dry(payload: dict):
    try:
        prompt = payload.get("prompt", "")
        logger.info(f"🚀 Starting plan_and_build with prompt: {prompt}")
        coordinator = AgentCoordinator()
        result = coordinator.plan_and_build(prompt)
        return {"result": result}
    except Exception as e:
        logger.error("Exception in /run-dry endpoint", exc_info=True)
        raise e
