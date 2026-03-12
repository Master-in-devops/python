# Git Essentials & Conflict Resolution

A quick-start guide to essential Git commands and manual conflict resolution.

---

## 🛠️ Core Commands

### 1. Project Setup
- `git init` : Start a new local repository.
- `git clone <url>` : Copy a remote project to your machine.
- `git config --global user.name "Name"` : Set your identity.

### 2. The Daily Workflow
- `git status` : See what has changed.
- `git add .` : Stage all changes for saving.
- `git commit -m "msg"` : Save staged changes to history.
- `git log --oneline` : Show a clean, short history.

### 3. Collaboration & GitHub
- `git remote add origin <url>` : Connect local repo to GitHub.
- `git push -u origin main` : Upload local saves to the cloud.
- `git pull` : Download and sync cloud changes to local.

---

## 🌿 Branching Logic

- `git branch` : List all local branches.
- `git checkout -b <name>` : Create and switch to a new branch.
- `git checkout <name>` : Switch back to an existing branch.
- `git merge <name>` : Pull code from `<name>` into your current branch.

---

## ⚠️ Merge Conflicts

### What is a Conflict?
It occurs when Git sees two different changes on the **same line** of the **same file** and cannot decide which one is correct.



### How to Resolve (Short Steps)
1. **Locate**: Run `git status` to find the "Unmerged paths".
2. **Open**: Open the file in your editor.
3. **Decide**: 
   - Code between `<<<<<<< HEAD` and `=======` is **Yours**.
   - Code between `=======` and `>>>>>>> branch` is **Theirs**.
4. **Edit**: Delete the markers (`<<<`, `===`, `>>>`) and keep the desired code.
5. **Finalize**:
   ```bash
   git add <filename>
   git commit -m "Resolved merge conflict"