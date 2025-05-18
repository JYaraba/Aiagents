# aiagents/agents/devopsagent.py

from aiagents.base.base_agent import BaseAgent
from aiagents.utils.file_writer import write_file
from aiagents.utils.progress_tracker import log_step

class DevOpsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="DevOpsAgent",
            role="Deployment Engineer",
            goal="Prepare Docker and deployment configs"
        )

    @log_step("DevOpsAgent", "Generating Docker and deployment configs")
    def execute(self, context: dict) -> dict:
        frontend_dockerfile = """\
# Frontend Dockerfile
FROM node:18
WORKDIR /app
COPY client/package*.json ./
RUN npm install
COPY client/ .
EXPOSE 3000
CMD ["npm", "start"]
"""

        backend_dockerfile = """\
# Backend Dockerfile
FROM node:18
WORKDIR /app
COPY server/package*.json ./
RUN npm install
COPY server/ .
EXPOSE 5000
CMD ["node", "src/server.js"]
"""

        docker_compose = """\
version: '3'
services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:3000"
    volumes:
      - ./client:/app
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "5000:5000"
    volumes:
      - ./server:/app
    depends_on:
      - mongo
  mongo:
    image: mongo
    ports:
      - "27017:27017"
"""

        gitignore = """\
node_modules/
.env
dist/
build/
.vscode/
__pycache__/
*.pyc
"""

        write_file("output/.gitignore", gitignore)
        write_file("output/Dockerfile.frontend", frontend_dockerfile)
        write_file("output/Dockerfile.backend", backend_dockerfile)
        write_file("output/docker-compose.yml", docker_compose)

        return {
            "docker": ["Dockerfile.frontend", "Dockerfile.backend", "docker-compose.yml"],
            "meta": "DevOps configs written"
        }
