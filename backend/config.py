import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MEMORY_TYPE: str = os.getenv("MEMORY_TYPE", "json")
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "output")

settings = Settings()
