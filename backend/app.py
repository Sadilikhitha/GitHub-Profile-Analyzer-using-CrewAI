from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from crew import crew

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static")


@app.get("/")
def home():
    return FileResponse("../frontend/index.html")


class GitHubRequest(BaseModel):
    github_username: str


@app.post("/analyze")
async def analyze(request: GitHubRequest):
    try:
        result = await crew.kickoff_async(
            inputs={
                "github_username": request.github_username
            }
        )

        return {
            "result": str(result)
        }

    except Exception as e:
        return {
        "result": None,
        "error": f"AI analysis failed: {str(e)}"
    }