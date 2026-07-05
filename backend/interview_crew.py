from crewai import Crew, Process

from agent import interview_agent
from tasks import interview_task

interview_crew = Crew(
    agents=[interview_agent],
    tasks=[interview_task],
    process=Process.sequential,
    verbose=True
)