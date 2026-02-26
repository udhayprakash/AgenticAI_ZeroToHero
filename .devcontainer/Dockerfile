FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    docker.io \
    jq \
    tmux \
    htop \
    ripgrep \
    && rm -rf /var/lib/apt/lists/*

# Install uv - fast Python package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Verify installations
RUN python --version && \
    uv --version

# Create workspace directory
WORKDIR /workspaces

# Set up environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    COLUMNS=200

# Optional: Download and setup Ollama (comment out if not needed)
# RUN curl -fsSL https://ollama.ai/install.sh | sh

LABEL maintainer="AgenticAI Development" \
      description="Development environment for Agentic AI applications"
