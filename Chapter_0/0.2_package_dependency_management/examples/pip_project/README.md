# Pip Project Example

Traditional pip + venv setup.

## Structure

```
pip_project/
├── .python-version      # Python version (3.11)
├── requirements.txt     # Dependencies list
├── requirements-dev.txt # Development dependencies
├── src/
│   └── app.py
└── tests/
    └── test_app.py
```

## Setup

```bash
# Create virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt --only-dev

# Add new package
pip install requests
pip freeze > requirements.txt  # Manual update!
```

## Pros
- ✅ Minimal tooling
- ✅ Works everywhere
- ✅ No learning curve

## Cons
- ❌ No lock file for reproducibility
- ❌ Manual requirements.txt management
- ❌ No built-in dev dependencies
- ❌ Slow version resolution
- ❌ No automatic venv creation
