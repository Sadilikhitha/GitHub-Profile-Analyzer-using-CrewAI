from crewai import Task
from agent import github_agent, interview_agent

# -----------------------------
# Task 1 : GitHub Analysis
# -----------------------------

research_task = Task(
    description="""
Analyze the GitHub profile of {github_username}.

You are an expert Technical Recruiter.

Carefully analyze the GitHub profile and repositories.

Generate a professional report using the following format.

# 👤 Developer Profile

- Name
- GitHub Username
- Bio (if available)
- Experience Level (Beginner / Intermediate / Advanced)
- Overall Developer Summary (4-5 lines)

# 💻 Technical Skills

Mention programming languages found from repositories.

Mention frameworks and libraries.

Mention databases.

Mention developer tools.

# 🛠 Technology Stack

Backend

Frontend

AI / ML

Database

Version Control

Cloud / Deployment (if any)

# 📂 Top Projects

Choose ONLY the best 3-5 repositories.

For every project include:

Project Name

Purpose

Technologies Used

Key Features

# ⭐ Strengths

Mention strengths based on repositories.

Examples:

• AI Development

• Backend Development

• REST API Development

• Problem Solving

• Project Organization

# 📈 Suggestions for Improvement

Mention 5 practical suggestions.

Example:

• Learn Docker

• Deploy projects

• Improve README

• Add Unit Testing

Only use information available from GitHub.

Never invent technologies or projects.

Format everything using proper Markdown.
""",

    expected_output="""
A structured professional GitHub profile report.
""",

    agent=github_agent
)

# -----------------------------
# Task 2 : Interview Preparation
# -----------------------------

interview_task = Task(
    description="""
You are a Senior Software Engineer at Google.

Using the following GitHub profile summary:

{summary}

Generate a personalized interview preparation guide.

Use the following format.

# 🎯 Technical Interview Questions

Generate 8 interview questions based ONLY on:

- Skills

- Technologies

- AI

- Backend

- APIs

- Databases

- System Design

For every question provide:

Question

Expected Answer (4-5 lines)

# 📚 Concepts to Revise

Mention important concepts the candidate should study.

Example:

FastAPI

REST APIs

CrewAI

LangGraph

Git

GitHub

Authentication

Deployment

Docker

# 💼 HR Interview Questions

Generate 5 professional HR questions.

Examples:

Tell me about yourself.

Describe your biggest project.

What challenge did you face?

Why should we hire you?

Where do you see yourself in 5 years?

# 🚀 Interview Tips

Provide 10 personalized interview tips.

Keep the output professional.

Use Markdown.

Do NOT ask repository-specific questions.

Focus on skills and technologies.

Do not invent information.
""",

    expected_output="""
A structured interview preparation guide.
""",

    agent=interview_agent
)