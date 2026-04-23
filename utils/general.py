# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

import requests
from PIL import Image


def download_uri(uri, dir="./"):
    """Downloads file from URI, performing checks and renaming; supports timeout and image format suffix addition."""
    # Download
    dir = Path(dir)
    f = dir / Path(uri).name  # filename
    response = requests.get(uri, timeout=10)
    response.raise_for_status()
    with open(f, "wb") as file:
        file.write(response.content)

    # Rename (remove wildcard characters)
    src = f  # original name
    f = Path(
        str(f)
        .replace("%20", "_")
        .replace("%", "_")
        .replace("*", "_")
        .replace("~", "_")
        .replace("(", "_")
        .replace(")", "_")
    )

    if "?" in str(f):
        f = Path(str(f)[: str(f).index("?")])

    if src != f:
        src.rename(f)  # rename

    # Add suffix (if missing)
    if not f.suffix:
        src = f  # original name
        f = f.with_suffix(f".{Image.open(f).format.lower()}")
        src.rename(f)  # rename
