# AI Developer Intelligence Platform

An AI-powered developer analysis platform that evaluates GitHub profiles and generates insights about developer skills, impact, and potential roles.

## Overview

This system analyzes a developer’s GitHub repositories and automatically generates a **Developer Intelligence Report** including:

* Repository activity
* Popularity and impact
* Programming language distribution
* Skill inference
* Recommended engineering roles
* Developer scoring metrics

The platform helps understand a developer's technical strengths based on their open-source contributions.

## Features

* GitHub repository analysis
* Automatic skill inference from languages and repository metadata
* Developer scoring algorithm
* Role recommendations (ML Engineer, Backend Engineer, Systems Engineer, etc.)
* Top repository extraction
* Language distribution visualization
* Developer skill radar chart
* Interactive dashboard

## Architecture

Backend API built using **FastAPI** that collects GitHub repository data and performs analysis.

Frontend dashboard built using **Streamlit** for interactive developer reports.

GitHub API → FastAPI Analysis Engine → Skill & Scoring Engine → Streamlit Dashboard

## Tech Stack

* Python
* FastAPI
* Streamlit
* GitHub REST API
* Matplotlib
* NumPy

## Example Output

The platform generates a developer report including:

* Developer score
* Skill breakdown
* Recommended roles
* Language distribution
* Top repositories

## Running the Project

Install dependencies:

pip install -r requirements.txt

Start the backend API:

python3 -m uvicorn app.main:app --reload

Run the dashboard:

streamlit run dashboard/app.py

## Example API Endpoint

http://127.0.0.1:8000/analyze/{github_username}

Example:

http://127.0.0.1:8000/analyze/torvalds

## Future Improvements

* Commit history analysis
* Code complexity metrics
* Pull request analysis
* ML-based developer scoring
* Organization-level analytics

## Author

John

