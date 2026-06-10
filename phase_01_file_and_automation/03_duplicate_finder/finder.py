import hashlib
from datetime import datetime
from pathlib import Path

here = Path(__file__).parent

folder = here / "folder"
folder.mkdir(exist_ok=True)

log_file = here / "finder.log"

duplicate_groups = 0
duplicate_files = 0


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(log_file, "a") as f:
        f.write(entry)
    print(entry, end="")


def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


hashes = {}

for file in folder.iterdir():
    if not file.is_file():
        continue

    h = get_file_hash(file)

    if h not in hashes:
        hashes[h] = []

    hashes[h].append(file.name)

for hash_value, files in hashes.items():
    if len(files) > 1:
        duplicate_files += len(files)
        duplicate_groups += 1
        log(f"Duplicate group found ({len(files)} files):")
        for file in files:
            log(f"  - {file}")

log(f"Scan complete — {duplicate_groups} duplicate groups, {duplicate_files} duplicate files")
