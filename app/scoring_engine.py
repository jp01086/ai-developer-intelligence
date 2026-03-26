def calculate_score(repo_count, total_stars, skills):

    activity_score = min(repo_count * 2, 30)
    impact_score = min(total_stars / 1000, 40)
    skill_diversity_score = min(len(skills) * 5, 30)

    developer_score = activity_score + impact_score + skill_diversity_score

    return {
        "developer_score": round(developer_score, 2),
        "activity_score": round(activity_score, 2),
        "impact_score": round(impact_score, 2),
        "skill_diversity_score": round(skill_diversity_score, 2)
    }