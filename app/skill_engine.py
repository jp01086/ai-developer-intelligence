from collections import Counter
import re

# keyword → skill mapping
SKILL_KEYWORDS = {
    "python": "Python",
    "java": "Java",
    "c++": "C++",
    "c": "C",
    "go": "Go",
    "rust": "Rust",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "react": "React",
    "node": "Node.js",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "tensorflow": "Machine Learning",
    "pytorch": "Machine Learning",
    "ml": "Machine Learning",
    "ai": "Artificial Intelligence",
    "linux": "Linux",
    "kernel": "Systems Programming",
    "api": "Backend Development",
    "backend": "Backend Development",
    "fastapi": "Backend Development",
    "django": "Backend Development",
    "flask": "Backend Development"
}


def infer_skills(languages):

    skills = []

    for lang in languages:
        if lang:
            skills.append(lang.lower())

    mapped_skills = []

    for word in skills:
        if word in SKILL_KEYWORDS:
            mapped_skills.append(SKILL_KEYWORDS[word])

    skill_counts = Counter(mapped_skills)

    return dict(skill_counts)


def infer_skills_from_metadata(repos):

    text_data = ""

    for repo in repos:

        name = repo.get("name", "")
        description = repo.get("description", "")
        topics = repo.get("topics", [])

        text_data += f"{name} {description} {' '.join(topics)} "

    text_data = text_data.lower()

    words = re.findall(r'\b[a-zA-Z\+\#]+\b', text_data)

    detected_skills = []

    for word in words:
        if word in SKILL_KEYWORDS:
            detected_skills.append(SKILL_KEYWORDS[word])

    skill_counts = Counter(detected_skills)

    return dict(skill_counts)


def merge_skills(lang_skills, metadata_skills):

    merged = Counter()

    merged.update(lang_skills)
    merged.update(metadata_skills)

    return dict(merged)


def recommend_roles(skills):

    roles = []

    if "Machine Learning" in skills or "Artificial Intelligence" in skills:
        roles.append("ML Engineer")

    if "Backend Development" in skills:
        roles.append("Backend Engineer")

    if "Systems Programming" in skills:
        roles.append("Systems Engineer")

    if "Docker" in skills or "Kubernetes" in skills:
        roles.append("DevOps Engineer")

    if not roles:
        roles.append("Software Engineer")

    return roles