# python
# Learning python
import os

dir_name = "learn"
file_name = "orginal.txt"
# Join the path and create the file
full_path = os.path.join(dir_name, file_name)

with open(full_path, "w") as f:
    f.write("Leaning devops!")
print ("file created successfully")
