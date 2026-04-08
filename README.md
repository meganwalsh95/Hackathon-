# Hackathon-

This repository contains the project structure for the application.
Prerequisites
- Install Python 3.10+ and ensure `python` is on your PATH.
- Git (to clone the repo).

Recommended folder structure

```
Hackathon-/
├─ .venv/               # local virtual environment (do not commit)
├─ src/                 # application source code
├─ tests/               # test suite
├─ requirements.txt     # pinned dependencies
├─ README.md
└─ .gitignore
```

Quick setup (Windows / PowerShell)

1. Clone the repo (if you haven't already):

```
git clone https://github.com/meganwalsh95/Hackathon-.git
cd Hackathon-
```

2. Create a virtual environment in the project root:

```
python -m venv .venv
```

3. Activate the virtual environment (PowerShell):

```
# If PowerShell blocks script execution, run as admin or set policy for current user:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
\.venv\Scripts\Activate.ps1
```

4. Upgrade pip and install dependencies:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you don't yet have a `requirements.txt` file, install packages you need and then pin them:

```
pip install <package1> <package2>
pip freeze > requirements.txt
```

Running the application

1. With the virtual environment activated, run the project's entrypoint. Replace the example below with the correct module/script for this project:

```
python -m src.main
# or
python src/main.py
```

Running tests

Install test dependencies (for example `pytest`) and run:

```
pip install pytest
pytest
```

.gitignore recommendations

Add the following (or generate one for Python) to avoid committing local environment files:

```
.venv/
__pycache__/
*.py[cod]
*.pyo
*.env
*.egg-info/
dist/
build/
```

Notes
- Keep `.venv` out of version control. Use `requirements.txt` to share dependencies.
- If you use Visual Studio or VS Code, configure the workspace to use the interpreter at `./.venv/Scripts/python.exe` (Windows) so the editor picks up the virtual environment.

If you want, I can also add a starter `.gitignore` and a `requirements.txt` skeleton to the repo.
