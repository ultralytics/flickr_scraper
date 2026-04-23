# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
from PIL import Image


def safe_filename_from_uri(uri):
    """Return a sanitized filename from a URI path without query parameters."""
    filename = unquote(Path(urlsplit(uri).path).name) or "download"
    return (
        filename.replace("%20", "_")
        .replace("%", "_")
        .replace("*", "_")
        .replace("~", "_")
        .replace("(", "_")
        .replace(")", "_")
        .replace(" ", "_")
    )


def download_uri(uri, dir="./"):
    """Downloads file from URI, performing checks and renaming; supports timeout and image format suffix addition."""
    # Download
    dir = Path(dir)
    f = dir / safe_filename_from_uri(uri)  # filename
    response = requests.get(uri, timeout=10)
    response.raise_for_status()
    with open(f, "wb") as file:
        file.write(response.content)

    # Add suffix (if missing)
    if not f.suffix:
        src = f  # original name
        f = f.with_suffix(f".{Image.open(f).format.lower()}")
        src.rename(f)  # rename
