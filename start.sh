#!/bin/bash

echo "Starting FastAPI backend..."
python3 -m uvicorn app.main:app --reload &

sleep 3

echo "Starting Streamlit dashboard..."
python3 -m streamlit run dashboard/app.py