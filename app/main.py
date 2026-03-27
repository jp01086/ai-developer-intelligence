from fastapi import FastAPI
import requests
from datetime import datetime
import os

from app.skill_engine import infer_skills, infer_skills_from_metadata, merge_skills, recommend_roles
from app.scoring_engine import calculate_score
from app.analysis_service import detect_frameworks
from app.commit_service import analyze_commit_activity
from app.code_analysis_service import analyze_code_complexity
from app.ai_summary_service import generate_ai_summary

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
    
    token = os.getenv("GITHUB_TOKEN")

    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "GitHub API request failed"}

    repos = response.json()
    if not isinstance(repos, list):
        return {"error": "GitHub API limit reached or invalid response"}

    frameworks = detect_frameworks(repos)
    commit_data = analyze_commit_activity(username, repos)
    code_analysis = analyze_code_complexity(repos)

    if not repos:
        return {"error": "User has no public repositories"}

    repo_count = len(repos)

    total_stars = 0
    languages = {}

    active_repos = 0
    latest_update = None

    for repo in repos:

        if not isinstance(repo, dict):
            continue

        total_stars += repo.get("stargazers_count", 0)

        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

        # activity tracking
        if repo.get("pushed_at"):
            active_repos += 1

            pushed_date = datetime.strptime(repo.get("pushed_at"), "%Y-%m-%dT%H:%M:%SZ")

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

    ai_summary = generate_ai_summary(username, languages, frameworks, skills)

    score_data = calculate_score(repo_count, total_stars, skills)

    score_breakdown = {
    "activity_score": commit_data["consistency_score"],
    "impact_score": min(total_stars / 1000, 100),
    "skill_diversity_score": len(languages) * 10
}
    
    return {
        "username": username,
        "repo_count": repo_count,
        "total_stars": total_stars,
        "languages": languages,
        "frameworks": frameworks,
        "skills": skills,
        "recommended_roles": roles,
        "developer_score": score_data["developer_score"],
        "score_breakdown": score_breakdown,

        "activity_analysis": {
        "active_repositories": active_repos,
        "last_active_days_ago": last_active_days
        },

        "top_repositories": top_repo_data,
        "commit_intelligence": commit_data,
        "code_complexity": code_analysis,
        "ai_summary": ai_summary
}
 