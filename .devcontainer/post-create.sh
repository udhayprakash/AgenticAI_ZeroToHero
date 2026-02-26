#!/bin/bash
# Post-create command - runs once when the container is created

set -e

echo "🛠️  Setting up AgenticAI development environment..."

# Update system packages
echo "📦 Updating system packages..."
apt-get update && apt-get upgrade -y

# Ensure uv is available
echo "⚡ Verifying uv installation..."
source $HOME/.cargo/env
uv --version

# Sync Python dependencies if pyproject.toml exists
if [ -f "pyproject.toml" ]; then
    echo "📚 Installing Python dependencies..."
    uv sync
fi

# Initialize git hooks if they exist
if [ -d ".git/hooks" ]; then
    echo "🔧 Setting up git hooks..."
    chmod +x .git/hooks/* 2>/dev/null || true
fi

echo "✅ Environment setup complete!"
echo ""
echo "📖 Quick start:"
echo "  - View documentation: open Chapter_0/README.md"
echo "  - Run FastAPI example: uv run python Chapter_0/0.3_fastapi_basics/basic_app.py"
echo "  - Run tests: uv run pytest Chapter_0/0.4_testing_quality/"
echo ""
