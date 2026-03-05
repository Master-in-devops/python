# for renaming the file
import os

dir_name = "learn"
file_name = "orginal.txt"
new_file_name = "duplicate.txt"

# Create the full paths for both the old and new names
old_full_path = os.path.join(dir_name, file_name)
new_full_path = os.path.join(dir_name, new_file_name)

# Check if the file exists before renaming to avoid FileNotFoundError
if os.path.exists(old_full_path):
    os.rename(old_full_path, new_full_path)
    print("Renamed the file successfully")
else:
    print("Error: The original file was not found.")