def generate_ai_summary(username, languages, frameworks, skills):

    lang_list = ", ".join(languages.keys())
    fw_list = ", ".join(frameworks) if frameworks else "various tools"
    skill_list = ", ".join(skills.keys())

    summary = (
        f"{username} appears to work primarily with {lang_list}. "
        f"The developer frequently uses technologies such as {fw_list}. "
        f"Key expertise areas include {skill_list}. "
        "Overall the profile suggests strong engineering activity and technical depth."
    )

    return summary