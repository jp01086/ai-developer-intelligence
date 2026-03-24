def infer_skills(languages):

    skills = []

    for lang in languages:

        if lang in ["Python", "Java", "Go"]:
            skills.append("Backend Development")

        if lang in ["C", "C++", "Rust"]:
            skills.append("Systems Programming")

        if lang in ["JavaScript", "TypeScript"]:
            skills.append("Frontend Development")

    return list(set(skills))

def recommend_roles(skills):

    roles = []

    if "Backend Development" in skills:
        roles.append("Backend Engineer")

    if "Systems Programming" in skills:
        roles.append("Systems Engineer")

    if "Frontend Development" in skills:
        roles.append("Frontend Engineer")

    return roles