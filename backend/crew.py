from agent import github_agent, writer_agent
from tasks import research_task, blog_writing_task
from crewai import Agent, Crew, Task, Process

crew = Crew(
    agents=[github_agent, writer_agent],
    tasks=[research_task, blog_writing_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff(
        inputs={
            "github_username": "Sadilikhitha"
        }
    )
    print(result)