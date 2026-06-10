import os
import shutil
from datetime import datetime
from pathlib import Path

here = Path(__file__).parent
workspace = here / "workspace"
log_file = workspace / "setup.log"

folders = ["documents", "images", "videos", "spreadsheets", "archives"]


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)


for folder in folders:
    folder_path = workspace / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    log(f"Folder {folder} created")
    print(f"Folder {folder} created")

# documents = workspace / "documents"
# images = workspace / "images"
# videos = workspace / "videos"
# spreadsheets = workspace / "spreadsheets"
# archives = workspace / "archives"

# documents.mkdir(parents=True, exist_ok=True)
# images.mkdir(parents=True, exist_ok=True)
# spreadsheets.mkdir(parents=True, exist_ok=True)
# videos.mkdir(parents=True, exist_ok=True)
# archives.mkdir(parents=True, exist_ok=True)

for i in range(1, 6):
    with open(f"{workspace}/file{i}.txt", "w") as f:
        f.write(f"written content in file {i}")
    print(f"File {workspace}/file{i}.txt created")
    log(f"File {workspace}/file{i}.txt created")

