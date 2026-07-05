from crewai import Crew, Process

from agent import github_agent
from tasks import research_task

summary_crew = Crew(
    agents=[github_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)