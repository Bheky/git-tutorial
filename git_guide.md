
# Git Guide for Project Source Control

Welcome to your **Git Source Control Guide**. This guide provides a complete walkthrough of how to use Git to manage and track your projects efficiently. This guide is especially helpful if you're working with **Python** or doing **web & app development**.

---

## Table of Contents

1. [What is Git?](#what-is-git)
2. [Installation](#installation)
3. [Basic Git Workflow](#basic-git-workflow)
4. [Common Git Commands](#common-git-commands)
5. [Working with Branches](#working-with-branches)
6. [Merging and Resolving Conflicts](#merging-and-resolving-conflicts)
7. [Working with Remote Repositories (e.g. GitHub)](#working-with-remote-repositories-eg-github)
8. [Git Best Practices](#git-best-practices)
9. [Useful Tips and Tricks](#useful-tips-and-tricks)
10. [Glossary](#glossary)

---

## What is Git?

**Git** is a distributed version control system that helps developers track changes in their codebase, collaborate with others, and manage project versions efficiently.

---

## Installation

### Windows / macOS / Linux:

Visit [https://git-scm.com](https://git-scm.com) and install Git for your system.

Verify installation:
```bash
git --version
```

---

## Basic Git Workflow

1. Initialize or clone a repository
2. Make changes to files (e.g. your Python scripts or HTML/CSS/JS files)
3. Stage the changes
4. Commit the changes with a message
5. Push the changes to a remote repository

---

## Common Git Commands

### Initialize a New Repository
```bash
git init
```

### Clone a Remote Repository
```bash
git clone https://github.com/username/repo.git
```

### Check Repository Status
```bash
git status
```

### Stage Files
```bash
git add filename
git add .
```

### Commit Changes
```bash
git commit -m "Add new feature to login system"
```

### View Commit History
```bash
git log
git log --oneline
```

---

## Working with Branches

```bash
git branch new-feature
git checkout new-feature
git checkout -b new-feature
git branch
git branch -d old-branch
```

---

## Merging and Resolving Conflicts

```bash
git checkout main
git merge new-feature
```

Manually resolve conflicts in files:
```diff
<<<<<<< HEAD
Your current code
=======
Incoming code
>>>>>>> new-feature
```

After resolving:
```bash
git add filename
git commit
```

---

## Working with Remote Repositories (GitHub)

```bash
git remote add origin https://github.com/username/repo.git
git push -u origin main
git pull origin main
```

---

## Git Best Practices

- Use `.gitignore` (for Python: `__pycache__/`, `.env`, `*.pyc`, `venv/`)
- Use feature branches
- Commit often with clear messages
- Pull before pushing to avoid conflicts

---

## Useful Tips and Tricks

### Sample `.gitignore` for Python/Web Projects
```
# Python
*.pyc
__pycache__/
venv/
.env

# Web
node_modules/
dist/
build/
*.log
```

### Stash Temporary Work
```bash
git stash
git stash pop
```

---

## Glossary

| Term | Description |
|------|-------------|
| Commit | Snapshot of your changes |
| Branch | Independent line of development |
| Remote | Hosted copy (e.g. GitHub) |
| Merge | Combine code from branches |

---

## Example Python Project Workflow

```bash
mkdir my_python_project && cd my_python_project
git init
echo "# My Python Project" > README.md
git add .
git commit -m "Initial commit"
git checkout -b feature/data-cleanup
# Work on scripts...
git add script.py
git commit -m "Add data cleaning script"
git push origin feature/data-cleanup
```

## Example Web App Workflow

```bash
npx create-react-app my-app
cd my-app
git init
git add .
git commit -m "Initial commit with React setup"
git checkout -b feature/navbar
# Edit Navbar.js...
git commit -am "Add responsive navbar"
git push origin feature/navbar
```

---

## Final Thoughts

Keep learning Git — it’s your best friend for collaboration, project management, and experimentation.

More resources:
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)

