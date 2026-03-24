from fastapi import FastAPI
import requests
from datetime import datetime

from app.skill_engine import infer_skills, infer_skills_from_metadata, merge_skills, recommend_roles
from app.scoring_engine import calculate_score

app = FastAPI(
    title="AI Developer Intelligence Platform",
    description="Analyzes GitHub developers and generates skill insights and developer score",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "AI Developer Intelligence Platform Running"}


@app.get("/analyze/{username}")
def analyze_user(username: str):

    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 404:
        return {"error": "GitHub user not found"}

    repos = response.json()

    if not repos:
        return {"error": "User has no public repositories"}

    repo_count = len(repos)

    total_stars = 0
    languages = {}

    active_repos = 0
    latest_update = None

    for repo in repos:

        total_stars += repo["stargazers_count"]

        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

        # activity tracking
        if repo["pushed_at"]:
            active_repos += 1

            pushed_date = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")

            if latest_update is None or pushed_date > latest_update:
                latest_update = pushed_date

    # calculate last active
    last_active_days = None
    if latest_update:
        last_active_days = (datetime.utcnow() - latest_update).days

    # get top repositories
    top_repos = sorted(
        repos,
        key=lambda x: x["stargazers_count"],
        reverse=True
    )[:5]

    top_repo_data = []

    for repo in top_repos:
        top_repo_data.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "description": repo["description"]
        })

    # skills from languages
    lang_skills = infer_skills(languages)

    # skills from metadata
    metadata_skills = infer_skills_from_metadata(repos)

    # merge skills
    skills = merge_skills(lang_skills, metadata_skills)

    roles = recommend_roles(skills)

    score_data = calculate_score(repo_count, total_stars, skills)

    return {
        "username": username,
        "repo_count": repo_count,
        "total_stars": total_stars,
        "languages": languages,
        "skills": skills,
        "recommended_roles": roles,
        "developer_score": score_data["developer_score"],
        "score_breakdown": score_data,

        "activity_analysis": {
            "active_repositories": active_repos,
            "last_active_days_ago": last_active_days
        },

        "top_repositories": top_repo_data
    }