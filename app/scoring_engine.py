def calculate_score(repo_count, total_stars):

    activity_score = min(repo_count * 5, 50)
    popularity_score = min(total_stars / 1000, 50)

    score = activity_score + popularity_score

    return round(score, 2)