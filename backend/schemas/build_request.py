from pydantic import BaseModel

class BuildRequest(BaseModel):
    prompt: str
