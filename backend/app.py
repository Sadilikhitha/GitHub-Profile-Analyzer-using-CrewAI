from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from summary_crew import summary_crew
from interview_crew import interview_crew

app = FastAPI()

app.mount("/static", StaticFiles(directory="../frontend"), name="static")


@app.get("/")
def home():
    return FileResponse("../frontend/index.html")


# ----------------------------
# Request Models
# ----------------------------

class GitHubRequest(BaseModel):
    github_username: str


class InterviewRequest(BaseModel):
    summary: str


# ----------------------------
# Endpoint 1 - GitHub Summary
# ----------------------------

@app.post("/analyze-summary")
async def analyze_summary(request: GitHubRequest):

    try:

        result = await summary_crew.kickoff_async(
            inputs={
                "github_username": request.github_username
            }
        )

        return {
            "success": True,
            "summary": str(result)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Summary generation failed: {str(e)}"
        )


# ----------------------------
# Endpoint 2 - Interview Prep
# ----------------------------

@app.post("/generate-interview")
async def generate_interview(request: InterviewRequest):

    try:

        result = await interview_crew.kickoff_async(
            inputs={
                "summary": request.summary
            }
        )

        return {
            "success": True,
            "interview": str(result)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Interview preparation failed: {str(e)}"
        )