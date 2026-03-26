#!/usr/bin/env bash

echo "Starting FastAPI backend..."

export PYTHONPATH=$PYTHONPATH:$(pwd)

python3 -m uvicorn app.main:app --host 0.0.0.0 --port $PORT