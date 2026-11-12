from datetime import datetime, timezone
from pathlib import Path

folder = Path(__file__).resolve().parent / "sample_collection"

print("Archive Atlas file inventory")
for item in sorted(folder.iterdir()):
    if item.is_file():
        file_info = item.stat()
        size_bytes = file_info.st_size
        modified_date = datetime.fromtimestamp(file_info.st_mtime, tz=timezone.utc).date()
        print(f"- {item.name} ({size_bytes} bytes) | Modified: {modified_date} UTC")