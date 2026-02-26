# .devcontainer - Development Container Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## Files

- **devcontainer.json** - Main configuration file for the development container
  - Specifies the Docker image/Dockerfile to use
  - Configures VS Code extensions
  - Sets up port forwarding
  - Defines initialization scripts

- **Dockerfile** - Custom Docker image for the development environment
  - Based on Microsoft's Python 3.11 image
  - Installs uv (fast Python package manager)
  - Installs Docker CLI for containerization
  - Sets up essential development tools

- **post-create.sh** - Initialization script
  - Runs once when container is first created
  - Updates system packages
  - Installs Python dependencies
  - Displays welcome message

- **post-start.sh** - Startup script
  - Runs each time container starts
  - Verifies environment setup
  - Shows quick status

## How It Works

1. **GitHub Codespaces** automatically detects this `.devcontainer/` folder
2. It builds the Dockerfile to create a consistent development environment
3. Installs VS Code extensions specified in devcontainer.json
4. Runs the post-create and post-start scripts
5. You get a fully configured development environment in the browser

## Key Features

✅ **Fast Python Setup** - uv is pre-installed (10-100× faster than pip)
✅ **Docker Support** - Docker-in-Docker for containerization
✅ **VS Code Extensions** - Python, Ruff, Pylance, Docker, Git
✅ **Port Forwarding** - 8000, 8080, 11434 (FastAPI, Ollama, etc.)
✅ **Reproducible** - Same environment for all developers

## Learning Materials

For detailed explanations and examples, see:
- [Chapter_0/0.1_python_dev_setup/](../Chapter_0/0.1_python_dev_setup/devcontainer.json) - Educational examples
- [Chapter_0/0.1_python_dev_setup/setup_guide.md](../Chapter_0/0.1_python_dev_setup/setup_guide.md) - Setup instructions

## Local Development with Devcontainer

You can also use this devcontainer locally with VS Code:

1. Install VS Code Dev Containers extension
2. Open the repository in VS Code
3. Press `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
4. VS Code will build and connect to the container

## Customization

To customize the development environment:

1. Edit `Dockerfile` to install additional tools
2. Edit `devcontainer.json` to change extensions or settings
3. Edit `post-create.sh` for custom initialization
4. Rebuild container: `Dev Containers: Rebuild Container`
