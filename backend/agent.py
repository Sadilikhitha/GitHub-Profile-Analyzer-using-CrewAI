from crewai import Agent, LLM
from tools import githubtool
import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()  # Load environment variables from .env file

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
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

writer_agent = Agent(
    role="Technical Blog Writer",
    goal="Create an engaging and professional blog post from the GitHub profile summary provided by the GitHub Profile Analyzer",
    backstory=(
        "You are a skilled technical content writer and developer advocate. You specialize "
        "in transforming technical information, project details, and developer achievements "
        "into compelling blog articles that are easy to read and engaging for a wide audience."
    ),
    llm=llm,
    tools = [githubtool]
)