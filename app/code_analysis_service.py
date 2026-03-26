def analyze_code_complexity(repos):

    repo_sizes = []

    for repo in repos[:10]:
        size = repo.get("size", 0)
        repo_sizes.append(size)

    if not repo_sizes:
        return {
            "avg_repo_size": 0,
            "complexity_level": "Low",
            "architecture_maturity": "Beginner"
        }

    avg_size = sum(repo_sizes) / len(repo_sizes)

    if avg_size < 200:
        complexity = "Low"
        maturity = "Beginner"

    elif avg_size < 1000:
        complexity = "Medium"
        maturity = "Growing"

    else:
        complexity = "High"
        maturity = "Advanced"

    return {
        "avg_repo_size": round(avg_size, 2),
        "complexity_level": complexity,
        "architecture_maturity": maturity
    }