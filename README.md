# AI Developer Intelligence Platform

An AI-powered analytics platform that evaluates GitHub developers and generates insights into their technical expertise, coding activity, and engineering impact.

The system analyzes GitHub repositories, commit activity, and project metadata to produce a **Developer Intelligence Report** including skill inference, developer scoring, and engineering insights.

---

# Overview

This platform analyzes a developer’s GitHub profile and automatically generates a comprehensive report including:

* Repository statistics
* Developer impact (stars and activity)
* Programming language distribution
* Skill inference from repositories
* Framework and technology detection
* Commit activity intelligence
* Code complexity estimation
* AI-generated developer summary
* Recommended engineering roles

The goal is to provide a **data-driven view of developer expertise** based on open-source contributions.

---

# Key Features

### Developer Analysis

* GitHub repository analysis
* Language distribution and technology usage
* Top repository insights

### Skill Intelligence

* Automatic skill inference from repositories and metadata
* Framework detection (FastAPI, Docker, React, etc.)
* Developer role recommendation engine

### Developer Scoring

A scoring algorithm that evaluates:

* Activity level
* Repository impact
* Skill diversity

### Commit Intelligence

* Commit activity analysis
* Active development months
* Consistency scoring

### Code Architecture Analysis

* Repository size estimation
* Code complexity categorization
* Architecture maturity evaluation

### AI Developer Summary

Automatically generates a concise description of a developer’s technical profile.

### Developer Comparison

Compare multiple GitHub developers based on their developer scores.

---

# System Architecture

```
GitHub REST API
        │
        ▼
FastAPI Backend (Developer Analysis Engine)
        │
        ▼
Skill Inference + Scoring Models
        │
        ▼
Developer Intelligence API
        │
        ▼
Streamlit Dashboard
```

---

# Tech Stack

Backend

* Python
* FastAPI

Frontend

* Streamlit

Data Processing

* GitHub REST API
* NumPy
* Matplotlib

---

# Running the Project

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start the backend API

```
python3 -m uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

### 3. Start the dashboard

```
python3 -m streamlit run dashboard/app.py
```

Open the dashboard at:

```
http://localhost:8501
```

---

# Example API Endpoint

Analyze a GitHub developer:

```
http://127.0.0.1:8000/analyze/{github_username}
```

Example:

```
http://127.0.0.1:8000/analyze/torvalds
```

---

# Example Output

The platform generates a developer report including:

* Developer score
* Skill profile
* Recommended engineering roles
* Language distribution
* Commit activity insights
* Code architecture analysis
* AI-generated developer summary

---

# Future Improvements

* Pull request analysis
* Contributor collaboration metrics
* Machine learning–based developer scoring
* Organization-level developer analytics
* Public deployment as a web application

---

# Author

John
<img width="674" height="736" alt="image" src="https://github.com/user-attachments/assets/1344942e-2782-44cb-9e32-44be3bf34f90" />

