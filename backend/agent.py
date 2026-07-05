from crewai import Agent, LLM
from tools import githubtool
import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()  # Load environment variables from .env file

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

github_agent = Agent(
    role="GitHub Profile Analyzer",
    goal="Analyze a GitHub profile and create a concise summary of the developer's skills, projects, technologies, and achievements",
    backstory=(
        "You are an expert GitHub analyst and technical recruiter with years of experience "
        "evaluating developer portfolios. You excel at identifying programming skills, "
        "project impact, technology stacks, contribution patterns, and career strengths "
        "from GitHub repositories and profile activity."
    ),
    llm=llm,
    tools = [githubtool]
)

interview_agent = Agent(
    role="Technical Interview Preparation Expert",
    goal="Generate personalized interview questions and preparation tips based on the developer's GitHub profile summary.",
    backstory=(
        "You are an experienced Software Engineering interviewer who has "
        "conducted hundreds of interviews for AI, Backend, Full Stack, and "
        "Software Developer roles. You analyze GitHub profiles to prepare "
        "candidates with relevant technical and HR interview questions."
    ),
    llm=llm
)