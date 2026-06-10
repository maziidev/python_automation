import os
import shutil
from datetime import datetime
from pathlib import Path

here = Path(__file__).parent
workspace = here / "workspace"

categories = {
    "documents": [".txt", ".docx", ".pdf"],
    "images": [".png", ".jpg", ".jpeg"],
    "spreadsheets": [".csv", ".xlsx"],
    "videos": [".mp4", ".mov", ".avi"]
}

for file in workspace.iterdir():
    if file.is_file():
        ext = file.suffix
        # print(file.name)
        # print(ext)

        for category, extensions in categories.items():
            if ext in extensions:
               destination = workspace / category
               destination.mkdir(exist_ok=True)
               shutil.move(str(file), str(destination / file.name))
               break






