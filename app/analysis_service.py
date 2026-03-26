def detect_frameworks(repos):
    frameworks = set()

    for repo in repos:
        name = repo["name"].lower()
        description = (repo["description"] or "").lower()

        text = name + " " + description

        if "react" in text:
            frameworks.add("React")

        if "fastapi" in text:
            frameworks.add("FastAPI")

        if "flask" in text:
            frameworks.add("Flask")

        if "django" in text:
            frameworks.add("Django")

        if "docker" in text:
            frameworks.add("Docker")

        if "tensorflow" in text:
            frameworks.add("TensorFlow")

    return list(frameworks)