#!/bin/bash

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$BASE_DIR"

# Setup venv if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
    # Installing directly here is fine since you only have 2 dependencies
    source venv/bin/activate && pip install textual rich
fi

source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:.

if [ -f "src/main.py" ]; then
    python3 src/main.py "$@"
else
    python3 main.py "$@"
fi
