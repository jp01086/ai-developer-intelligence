import requests
from datetime import datetime
from collections import defaultdict


def analyze_commit_activity(username, repos):

    weekly_commits = 0
    active_months = set()

    for repo in repos[:5]:  # limit to avoid GitHub rate limits
        repo_name = repo["name"]

        url = f"https://api.github.com/repos/{username}/{repo_name}/commits"

        response = requests.get(url)

        if response.status_code != 200:
            continue

        commits = response.json()

        weekly_commits += len(commits)

        for commit in commits:
            date = commit["commit"]["author"]["date"]
            month = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m")

            active_months.add(month)

    consistency_score = min(len(active_months) * 5, 30)

    return {
        "commits_last_week": weekly_commits,
        "active_months": len(active_months),
        "consistency_score": consistency_score
    }