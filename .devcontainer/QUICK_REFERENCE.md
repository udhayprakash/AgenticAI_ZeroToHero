# 🚀 Development Environment Quick Reference

## GitHub Codespaces (Recommended for Learning)

### Start a Codespace
1. Click green **Code** button on GitHub
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. Wait 2-3 minutes for setup

**That's it!** You now have:
- ✅ Python 3.11
- ✅ uv package manager
- ✅ Docker CLI
- ✅ All VS Code extensions configured
- ✅ Ports forwarded (8000, 8080, 11434)

### Using Your Codespace

```bash
# Install dependencies
uv sync

# Run FastAPI server
uv run python Chapter_0/0.3_fastapi_basics/basic_app.py
# → Visit http://localhost:8000/docs

# Run tests
uv run pytest Chapter_0/0.4_testing_quality/ -v

# Add a package
uv add fastapi

# Check what's installed
uv pip list
```

### Stop/Restart Codespace
- **Stop:** Codespace → Stop (saves resources)
- **Restart:** Codespaces dropdown → Your codespace → Resume

---

## Local Development (Advanced)

### Prerequisites
- VS Code with "Dev Containers" extension
- Docker Desktop running

### Setup
1. Clone repository
2. Open in VS Code
3. Click "Dev Containers" button (bottom left)
4. Select "Reopen in Container"
5. Wait for container to build

### What's the Same?
- Same environment as Codespaces
- Same commands work
- Same extensions installed

---

## The Devcontainer Files

Located in `/.devcontainer/`:

| File | What It Does |
|------|-------------|
| `devcontainer.json` | Configuration (extensions, ports, etc.) |
| `Dockerfile` | Builds the container image |
| `post-create.sh` | Runs once to initialize |
| `post-start.sh` | Runs each time container starts |
| `README.md` | Detailed documentation |

For learning what these do, see:
📚 [Chapter_0/0.1_python_dev_setup/](../Chapter_0/0.1_python_dev_setup/)

---

## Common Commands

### Start Developing
```bash
uv sync              # Install dependencies
uv run python app.py # Run your code
uv add requests      # Add a package
```

### Run Examples
```bash
# FastAPI
uv run python Chapter_0/0.3_fastapi_basics/basic_app.py

# Tests
uv run pytest Chapter_0/0.4_testing_quality/

# Property-based tests
uv run pytest Chapter_0/0.4_testing_quality/test_property_based.py -v
```

### Debugging
```bash
python --version           # Check Python
uv --version              # Check uv
docker --version          # Check Docker
pip list                  # Check packages
uv pip list               # Same thing (via uv)
```

---

## Troubleshooting

### Codespace Won't Start
- Click "Rebuild container" button
- Wait for full rebuild

### Dependencies Not Installed
```bash
uv sync
```

### Port Not Accessible
- Check "Ports" tab in Codespace
- Ports 8000, 8080, 11434 should be there

### Out of Storage
- Codespaces have 32GB disk
- Check: `df -h`
- Delete old experiment folders if needed

---

## Learning Path

📖 **Start here:**
1. [Chapter_0/README.md](../Chapter_0/README.md) - Course overview
2. [Chapter_0/0.1_python_dev_setup/](../Chapter_0/0.1_python_dev_setup/) - Understand your environment
3. [Chapter_0/0.2_package_dependency_management/](../Chapter_0/0.2_package_dependency_management/) - Learn uv
4. [Chapter_0/0.3_fastapi_basics/](../Chapter_0/0.3_fastapi_basics/) - Build APIs
5. [Chapter_0/0.4_testing_quality/](../Chapter_0/0.4_testing_quality/) - Write tests

---

## What's Pre-installed

### System Tools
- Python 3.11
- uv (fast package manager)
- Docker CLI (can build/run containers)
- git, curl, wget, jq, tmux, htop

### VS Code Extensions
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Ruff (charliermarsh.ruff)
- Docker (ms-docker.docker)
- Git Graph
- Debugpy

### Port Forwarding
- **8000** → FastAPI, Uvicorn servers
- **8080** → Web APIs
- **11434** → Ollama (local LLMs)

---

## Need to Customize?

Want to add a tool or package permanently?

1. **For temporary use:**
   ```bash
   uv add package_name
   ```

2. **For permanent (in Dockerfile):**
   Edit `/.devcontainer/Dockerfile`, then rebuild

3. **For VS Code settings:**
   Edit `/.devcontainer/devcontainer.json`, then rebuild

---

**Happy coding! 🎉**
