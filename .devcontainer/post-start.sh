#!/bin/bash
# Post-start command - runs each time the container starts

echo "🚀 AgenticAI development environment ready!"

# Verify Python and uv are available
echo "Python: $(python --version)"
echo "uv: $(uv --version)"

# Optional: Check if dependencies are installed
if [ -d ".venv" ]; then
    echo "✅ Virtual environment detected"
else
    echo "⚠️  Virtual environment not found. Run 'uv sync' to install dependencies"
fi

echo ""
