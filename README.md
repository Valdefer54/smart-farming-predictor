# Final Project — Crop Prediction System

This repository contains a small Flask application that loads a machine learning model (Random Forest) to recommend crops based on soil and weather features.

**Project Structure**
- `main.py`: Flask server and API endpoints.
- `ui/templates/inteface.html`: web interface to enter data and view recommendations.
- `model_ml/random_forest_model.joblib`: the trained model file (binary).
- `model_ml/predict.py`: helper functions to load the model and predict.

**Requirements**
- Python 3.10+ (or the Python version you use in your virtual environment)
- pip

Recommended dependencies (if you don't have a `requirements.txt`):
- `Flask`
- `joblib`
- `pandas`
- `scikit-learn` (only if you plan to retrain or inspect the model)

**Instructions (Windows / PowerShell)**

1) Open PowerShell in the project folder (example):

```powershell
cd "C:\Users\Usuario\Desktop\Proyecto Final Programación III"
```

2) Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Install dependencies (if you have a `requirements.txt`):

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the core dependencies:

```powershell
pip install flask joblib pandas scikit-learn
```

4) Run the application:

```powershell
python .\main.py
# Open the interface in your browser
Start-Process http://127.0.0.1:5000
```

5) Test the endpoint from the web interface: fill the form and press `ANALYZE SOIL`. The HTML posts to `/predecir` and expects a JSON response containing `status: 'success'`.

**Push the repository to GitHub**

Minimal steps to create a remote repository and push your code (PowerShell):

1. Initialize git, add files and commit:

```powershell
git init
git add .
git commit -m "Initial: crop predictor project"
```

2. Create a repository on GitHub (options):
- Option A (web): create a new repository at https://github.com/new and copy the remote URL.
- Option B (gh CLI, if you have it):

```powershell
gh repo create REPO_NAME --public --source . --remote origin --push
```

3. If you created the repo on the web, add the remote and push:

```powershell
# Replace <REMOTE_URL> with the URL GitHub gives you (HTTPS or SSH)
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

**Important recommendations before pushing**
- Avoid committing large binary files (for example, the trained model) if you don't want the repository to grow too large. Consider using `git-lfs` for `random_forest_model.joblib`.
- Create a `.gitignore` file that at minimum contains:

```
.venv/
__pycache__/
*.pyc
model_ml/*.joblib
.env
```

Commands to create `.gitignore` and commit it:

```powershell
# Create .gitignore (you can edit it later)
@"
.venv/
__pycache__/
*.pyc
model_ml/*.joblib
.env
"@ > .gitignore

git add .gitignore
git commit -m "Add .gitignore"
```

**Additional notes**
- If `model_ml/random_forest_model.joblib` should be tracked but is large, use Git LFS instead of normal git. Example workflow:


- If you ever move the templates folder, Flask supports specifying the templates directory with `template_folder`, e.g. `Flask(__name__, template_folder='ui/templates')` (already configured in `main.py`).

If you want, I can also:
- Generate a `requirements.txt` automatically from the environment.
- Add a `.gitattributes` file and set up Git LFS for you.
- Create the GitHub repository using the `gh` CLI if you give me the desired repository name.

README translated and updated. If you'd like, I can also create `requirements.txt` and a `.gitignore` file now.
