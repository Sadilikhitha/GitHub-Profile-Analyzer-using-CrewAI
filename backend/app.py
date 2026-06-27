from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from crew import crew
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("../frontend/index.html")


class GitHubRequest(BaseModel):
    github_username: str


@app.post("/analyze")
async def analyze(request: GitHubRequest):
    result = await crew.kickoff_async(
        inputs={
            "github_username": request.github_username
        }
    )

    return {"result": str(result)}