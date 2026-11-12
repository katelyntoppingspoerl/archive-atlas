# Archive Atlas

A Python tool for inventorying digital collections and recording file metadata. It lists the files directly inside a folder and reports each filename, size in bytes, file extension and last-modified date in UTC.

## Quick start

Open the repository in GitHub Codespaces, or use a local terminal with Python 3. Run these commands from the repository folder. The script uses Python’s standard library, so there are no extra packages to install.

**Scan the included sample collection**

```bash
python3 inventory.py
```

You should see `interview-notes.txt` and `photo-record.txt`, each with a size and a modification date.

**Scan a folder you choose**

```bash
python3 inventory.py "/path/to/your/collection"
```

Replace `/path/to/your/collection` with your folder’s path. Use `.` to scan the current folder.

**Export the sample inventory to CSV**

```bash
python3 inventory.py --csv sample-inventory.csv
```

Open `sample-inventory.csv` in a spreadsheet app to view the filename, size_bytes, modified_date_utc, and extension  columns. Each export needs a new filename because Archive Atlas protects existing files from being overwritten.