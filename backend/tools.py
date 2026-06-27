from crewai.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@tool("GitHub Profile Tool")
def githubtool(username: str) -> str:
    """Fetch GitHub profile details."""

    token = os.getenv("GITHUB_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    user = requests.get(
        f"https://api.github.com/users/{username}",
        headers=headers
    ).json()

    repos = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers=headers
    ).json()

    summary = f"""
    Name: {user.get('name')}
    Bio: {user.get('bio')}
    Public Repositories: {user.get('public_repos')}

    Repositories:
    """

    for repo in repos[:10]:
        summary += f"- {repo['name']}: {repo.get('description')}\n"

    return summary