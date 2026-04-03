import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

API_URL = "https://ai-developer-intelligence.onrender.com/analyze"

st.set_page_config(page_title="AI Developer Intelligence", layout="wide")

st.title("AI Developer Intelligence Platform")

st.markdown(
"""
Analyze GitHub developers using AI-powered metrics including:

• Activity Score  
• Code Impact  
• Skill Diversity  
• Commit Intelligence  
• Architecture Maturity
"""
)

# -------------------------------------------------
# Developer Analysis
# -------------------------------------------------

username = st.text_input("Enter GitHub Username")

if st.button("Analyze Developer"):

    if username.strip() == "":
        st.warning("Please enter a GitHub username.")
        st.stop()

    with st.spinner("Analyzing developer..."):

        try:
            response = requests.get(f"{API_URL}/{username}", timeout=30)

            if response.status_code != 200:
                st.error("Backend API error")
                st.stop()

            data = response.json()

            if "username" not in data:
                st.error("Invalid response from API")
                st.write(data)
                st.stop()

        except Exception as e:
            st.error("Backend API unreachable or waking up.")
            st.write(e)
            st.stop()

    st.divider()

    # -------------------------------------------------
    # Developer Basic Info
    # -------------------------------------------------

    st.header("Developer Report")

    col1, col2, col3 = st.columns(3)

    col1.metric("Repositories", data["repo_count"])
    col2.metric("Total Stars", data["total_stars"])
    col3.metric("Developer Score", data["developer_score"])

    # -------------------------------------------------
    # Score Breakdown
    # -------------------------------------------------

    st.subheader("Score Breakdown")

    score = data["score_breakdown"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Activity Score", score["activity_score"])
    col2.metric("Impact Score", score["impact_score"])
    col3.metric("Skill Diversity", score["skill_diversity_score"])

    # -------------------------------------------------
    # AI Summary
    # -------------------------------------------------

    st.subheader("AI Developer Summary")
    st.write(data["ai_summary"])

    # -------------------------------------------------
    # Commit Intelligence
    # -------------------------------------------------

    st.subheader("Commit Activity")

    commit = data["commit_intelligence"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Commits Last Week", commit["commits_last_week"])
    col2.metric("Active Months", commit["active_months"])
    col3.metric("Consistency Score", commit["consistency_score"])

    # -------------------------------------------------
    # Code Architecture
    # -------------------------------------------------

    st.subheader("Code Architecture Analysis")

    code = data["code_complexity"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Repo Size", round(code["avg_repo_size"], 2))
    col2.metric("Complexity Level", code["complexity_level"])
    col3.metric("Architecture Maturity", code["architecture_maturity"])

    # -------------------------------------------------
    # Skills
    # -------------------------------------------------

    st.subheader("Skills")

    skills = data["skills"]
    st.write(skills)

    # -------------------------------------------------
    # Skill Radar Chart
    # -------------------------------------------------

    if skills:

        st.subheader("Developer Skill Profile")

        labels = list(skills.keys())
        values = list(skills.values())

        max_value = max(values)
        values = [v / max_value for v in values]

        values.append(values[0])

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles.append(angles[0])

        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        st.pyplot(fig)

    # -------------------------------------------------
    # Recommended Roles
    # -------------------------------------------------

    st.subheader("Recommended Roles")
    st.write(data["recommended_roles"])

    # -------------------------------------------------
    # Language Distribution
    # -------------------------------------------------

    languages = data["languages"]

    if languages:

        st.subheader("Language Distribution")

        labels = list(languages.keys())
        values = list(languages.values())

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%")

        st.pyplot(fig)

    # -------------------------------------------------
    # Top Repositories
    # -------------------------------------------------

    st.subheader("Top Repositories")

    for repo in data["top_repositories"]:

        st.markdown(
        f"""
### {repo['name']}

⭐ Stars: {repo['stars']}  
💻 Language: {repo['language']}  
📝 {repo['description']}
"""
        )

st.divider()

# -------------------------------------------------
# Developer Comparison
# -------------------------------------------------

st.header("Developer Comparison")

user1 = st.text_input("Developer 1")
user2 = st.text_input("Developer 2")
user3 = st.text_input("Developer 3")

if st.button("Compare Developers"):

    users = [user1, user2, user3]
    scores = []

    with st.spinner("Comparing developers..."):

        for u in users:

            if u:

                try:
                    res = requests.get(f"{API_URL}/{u}", timeout=30)
                    data = res.json()

                    if "developer_score" in data:
                        scores.append(data["developer_score"])
                    else:
                        scores.append(0)

                except:
                    scores.append(0)

            else:
                scores.append(0)

    labels = [user1 or "Empty", user2 or "Empty", user3 or "Empty"]

    fig, ax = plt.subplots()

    ax.bar(labels, scores)

    ax.set_title("Developer Score Comparison")
    ax.set_ylabel("Score")

    st.pyplot(fig)
