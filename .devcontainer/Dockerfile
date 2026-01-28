FROM mcr.microsoft.com/devcontainers/base:ubuntu

# System dependencies
RUN apt-get update && apt-get install -y \
    curl wget git jq netcat-openbsd \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Claude Code CLI
RUN npm install -g @anthropic-ai/claude-code || true

# Create directories
RUN mkdir -p /root/.claude/tasks /workspace

WORKDIR /workspace
