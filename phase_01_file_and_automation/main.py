import os
import shutil
from pathlib import Path

# Create a directory
os.makedirs("test_folder/subfolder", exist_ok=True)

# Rename a file
os.rename("old_name.txt", "new_name.txt")

# Delete a file
os.remove("file.txt")

# Delete an empty folder
os.rmdir("empty_folder")

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Move a file
shutil.move("source.txt", "new_location/source.txt")

# Copy entire folder
shutil.copytree("source_folder", "destination_folder")

# Delete entire folder and contents
shutil.rmtree("folder_to_delete")