import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path

default_folder = Path(__file__).resolve().parent / "sample_collection"

parser = argparse.ArgumentParser(description="List files and their metadata.")
parser.add_argument("folder", nargs="?", type=Path, default=default_folder)
parser.add_argument("--csv", type=Path, help="Save the inventory to a new CSV file.")
args = parser.parse_args()

folder = args.folder
if not folder.is_dir():
    parser.error(f"Folder does not exist or is not a directory: {folder}")

rows = []
print("Archive Atlas file inventory")
for item in sorted(folder.iterdir()):
    if item.is_file():
        file_info = item.stat()
        size_bytes = file_info.st_size
        modified_date = datetime.fromtimestamp(file_info.st_mtime, tz=timezone.utc).date()
        extension = item.suffix
        rows.append((item.name, size_bytes, modified_date, extension))
        print(
            f"- {item.name} ({size_bytes} bytes) | Modified: {modified_date} UTC"
            f" | Extension: {extension or '(none)'}"
        )

if args.csv is not None:
    try:
        with args.csv.open("x", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["filename", "size_bytes", "modified_date_utc", "extension"])
            writer.writerows(rows)
    except OSError as error:
        parser.error(f"Could not create CSV: {error}")
    print(f"Saved CSV to {args.csv}")