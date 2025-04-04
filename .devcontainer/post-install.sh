git config --global --add safe.directory /workspaces/*
python3 -m venv ~/.virtualenvs/poetry
source ~/.virtualenvs/poetry/bin/activate
poetry install
pre-commit install
