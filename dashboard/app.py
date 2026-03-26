import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

st.title("AI Developer Intelligence Platform")

username = st.text_input("Enter GitHub Username")

if st.button("Analyze Developer"):

    url = f"https://ai-developer-intelligence.onrender.com/analyze/{username}"
    try:
        response = requests.get(url)
        data = response.json()
    except:
        st.error("Backend API is not running yet.")
        st.stop()

    st.subheader("Developer Report")

    st.write("Username:", data["username"])
    st.write("Repo Count:", data["repo_count"])
    st.write("Total Stars:", data["total_stars"])
    st.write("Developer Score:", data["developer_score"])

    # ----------------------------
    # Score Breakdown
    # ----------------------------

    st.subheader("Score Breakdown")

    score = data["score_breakdown"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Activity Score", score["activity_score"])
    col2.metric("Impact Score", score["impact_score"])
    col3.metric("Skill Diversity", score["skill_diversity_score"])

    #-------------------------------
    # AI Summary
    #-------------------------------

    st.subheader("AI Developer Summary")
    st.write(data["ai_summary"])
   
    #------------------------------
    # Commit intelligence
    #------------------------------

    st.subheader("Commit Activity")

    commit = data["commit_intelligence"]

    st.write(f"Commits Last Week: {commit['commits_last_week']}")
    st.write(f"Active Months: {commit['active_months']}")
    st.write(f"Consistency Score: {commit['consistency_score']}")

    # ----------------------------
    # Code Architecture Analysis
    # ----------------------------

    st.subheader("Code Architecture Analysis")

    code = data["code_complexity"]

    st.write(f"Average Repo Size: {round(code['avg_repo_size'], 2)}")
    st.write(f"Complexity Level: {code['complexity_level']}")
    st.write(f"Architecture Maturity: {code['architecture_maturity']}")
   
    # ----------------------------
    # Skills
    # ----------------------------

    st.subheader("Skills")
    st.write(data["skills"])

    # ----------------------------
    # Skill Radar Chart
    # ----------------------------

    if data["skills"]:

        st.subheader("Developer Skill Profile")

        skills = data["skills"]

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

    # ----------------------------
    # Recommended Roles
    # ----------------------------

    st.subheader("Recommended Roles")
    st.write(data["recommended_roles"])

    # ----------------------------
    # Language Distribution
    # ----------------------------

    languages = data["languages"]

    if languages:
        st.subheader("Language Distribution")

        labels = list(languages.keys())
        values = list(languages.values())

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%")

        st.pyplot(fig)

    # ----------------------------
    # Top Repositories
    # ----------------------------

    st.subheader("Top Repositories")

    for repo in data["top_repositories"]:
        st.markdown(f"""
### {repo['name']}

⭐ Stars: {repo['stars']}  
💻 Language: {repo['language']}  
📝 {repo['description']}
""")
        
        st.header("Developer Comparison")

user1 = st.text_input("Developer 1")
user2 = st.text_input("Developer 2")
user3 = st.text_input("Developer 3")

if st.button("Compare Developers"):

    users = [user1, user2, user3]
    scores = []

    for u in users:
        if u:
            url = f"https://ai-developer-intelligence.onrender.com/analyze/{u}"
            res = requests.get(url)
            data = res.json()
            if "developer_score" in data:
              scores.append(data["developer_score"])
            else:
              scores.append(0)
        else:
            scores.append(0)

    labels = [user1, user2, user3]

    fig, ax = plt.subplots()
    ax.bar(labels, scores)

    ax.set_title("Developer Score Comparison")
    ax.set_ylabel("Score")

    st.pyplot(fig)