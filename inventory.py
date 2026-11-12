from pathlib import Path

folder = Path(__file__).resolve().parent

print("Archive Atlas file inventory")
for item in sorted(folder.iterdir()):
    if item.is_file():
        print(f"- {item.name}")
