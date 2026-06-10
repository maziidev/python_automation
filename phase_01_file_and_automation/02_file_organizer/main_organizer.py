import shutil
from pathlib import Path

here = Path(__file__).parent
workspace = here / "workspace"

categories = {
    "documents": {
        "pdfs": [".pdf"],
        "docs": [".txt", ".docx", ".doc", ".epub", ".ppt", ".pptx"],
        "programming": {
            "python": [".py"],
            "js_ts": [".js", ".ts"],
            "java": [".java"],
            "c_cpp": [".c", ".cpp"],
            "rust": [".rs"],
            "golang": [".go"]
        }
    },
    "images": {
        "pngs": [".png"],
        "jpgs": [".jpg"],
        "jpegs": [".jpeg"],
        "svgs": [".svg"],
        "webps": [".webp"],
    },
    "spreadsheets": {
        "csvs": [".csv"],
        "excel": [".xlsx"],
    },
    "videos": {
        "mp4": [".mp4"],
        "mkv": [".mkv"],
        "avi": [".avi"],
        "mov": [".mov"],
    },
    "music": {
        "mp3": [".mp3"],
        "wav": [".wav"]
    },
    "executables": {
        "windows": [".exe"],
        "linux": [".tar", ".deb", ".sh"]
    },
}

summary = {category: 0 for category in categories}
summary["others"] = 0

for file in workspace.iterdir():
    if not file.is_file():
        continue

    ext = file.suffix.lower()
    moved = False

    for category, subcategories in categories.items():
        if moved:
            break
        for subcat, value in subcategories.items():
            if moved:
                break
            if isinstance(value, list):
                if ext in value:
                    destination = workspace / category / subcat
                    destination.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file), destination / file.name)
                    print(f"Moved {file.name} -> {category}/{subcat}")
                    summary[category] += 1
                    moved = True
            elif isinstance(value, dict):
                for lang, extensions in value.items():
                    if ext in extensions:
                        destination = workspace / category / subcat / lang
                        destination.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(file), destination / file.name)
                        print(f"Moved {file.name} -> {category}/{subcat}/{lang}")
                        summary[category] += 1
                        moved = True
                        break

    if not moved:
        others = workspace / "others"
        others.mkdir(exist_ok=True)
        shutil.move(str(file), others / file.name)
        print(f"Unrecognized: {file.name} -> others/")
        summary["others"] += 1

print("\n--- Summary ---")
for category, count in summary.items():
    print(f"{category}: {count} files")
