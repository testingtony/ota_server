FROM mcr.microsoft.com/devcontainers/python:3.12

USER vscode
WORKDIR /home/vscode
RUN pipx install poetry  &&  \
    pipx inject poetry "poetry-dynamic-versioning[plugin]"
