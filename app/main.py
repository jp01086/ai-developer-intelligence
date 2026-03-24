from fastapi import FastAPI
import requests
from skill_engine import infer_skills
from scoring_engine import calculate_score
from skill_engine import infer_skills, recommend_roles

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
    repos = response.json()

    repo_count = len(repos)

    total_stars = 0
    languages = {}

    for repo in repos:
        total_stars += repo["stargazers_count"]

        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    skills = infer_skills(languages)
    roles = recommend_roles(skills)
    score = calculate_score(repo_count, total_stars)

    return {
    "username": username,
    "repo_count": repo_count,
    "total_stars": total_stars,
    "languages": languages,
    "skills": skills,
    "recommended_roles": roles,
    "developer_score": score
}