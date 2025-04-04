FROM mcr.microsoft.com/devcontainers/python:3.12

USER vscode
WORKDIR /home/vscode
RUN pipx install poetry  &&  \
  pipx inject poetry "poetry-dynamic-versioning[plugin]"

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-$(arch).zip" -o "awscliv2.zip" && \
  unzip awscliv2.zip && \
  sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update && \
  rm -rf aws awscliv2.zip

RUN wget https://github.com/cli/cli/releases/download/v2.69.0/gh_2.69.0_linux_$(dpkg --print-architecture).deb && \
  sudo dpkg -i gh_2.69.0_linux_arm64.deb && \
  rm gh_2.69.0_linux_arm64.deb
