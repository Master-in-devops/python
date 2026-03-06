# Python `os` Module: Features and Capabilities

The `os` module provides a portable way of using operating system-dependent functionality. It allows your Python scripts to interact with the file system, manage processes, and handle environment variables regardless of whether you are running on Windows, macOS, or Linux.

## 1. Directory Navigation and Exploration
These functions allow a script to "sense" its location and explore the surrounding folder structure.

* **`os.getcwd()`**: Returns the **Current Working Directory** as a string.
* **`os.chdir(path)`**: Changes the current directory to the specified `path`.
* **`os.listdir(path='.')`**: Returns a list of all files and folders inside the specified directory.
* **`os.walk(top)`**: Generates file names in a directory tree by walking either top-down or bottom-up.



---

## 2. File and Folder Manipulation (CRUD)
Standard operations for creating, renaming, and deleting system objects.

| Function | Description |
| :--- | :--- |
| **`os.mkdir()`** | Creates a single directory. |
| **`os.makedirs()`** | Creates a directory and all necessary intermediate parent directories. |
| **`os.remove()`** | Deletes a specific file. |
| **`os.rmdir()`** | Deletes an **empty** directory. |
| **`os.rename()`** | Renames or moves a file or directory. |

---

## 3. Path Management (`os.path`)
The `os.path` sub-module is essential for handling file paths strings in a way that remains compatible across different operating systems.

* **`os.path.join(path, *paths)`**: Joins folder names using the correct system separator (`/` or `\`).
* **`os.path.exists(path)`**: Checks if a file or directory actually exists on the disk.
* **`os.path.isfile()` / `os.path.isdir()`**: Identifies if a path points to a file or a folder.
* **`os.path.splitext(path)`**: Splits the file path into a pair `(root, ext)`, making it easy to find file extensions.
* **`os.path.getsize(path)`**: Returns the size of the file in bytes.



---

## 4. System and Environment Interaction
Tools for interacting with the underlying OS shell and configuration settings.

* **`os.environ`**: A dictionary-like object containing all system environment variables. Useful for retrieving API keys or configuration strings.
* **`os.name`**: Identifies the OS interface ('posix' for Linux/Mac, 'nt' for Windows).
* **`os.system(command)`**: Executes a shell command (e.g., `os.system('cls')` to clear the terminal).
* **`os.getpid()`**: Returns the unique Process ID of the current Python script.

---

## Usage Example: Safe Path Creation
```python
import os

# Securely creating a path and directory
folder_name = "data_exports"
file_name = "report.csv"

full_path = os.path.join(os.getcwd(), folder_name, file_name)

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Created directory: {folder_name}")

print(f"Target file path: {full_path}")
