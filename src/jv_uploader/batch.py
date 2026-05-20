from pathlib import Path
from .pipeline import process_jv_file

def upload_all_jv(root: str):
    root = Path(root)
    files = list(root.rglob("*.txt"))

    for f in files:
        print(f"Uploading {f}")
        process_jv_file(str(f))
