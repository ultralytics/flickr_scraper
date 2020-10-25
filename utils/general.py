# General utilities for use in image-handling operations
# Written by Glenn Jocher (glenn.jocher@ultralytics.com) for https://github.com/ultralytics

import os
from pathlib import Path

import requests
from PIL import Image


def download_uri(uri, dir='./'):
    # Download a file from a given URI, including minimal checks

    # Download
    f = dir + os.path.basename(uri)  # filename
    with open(f, 'wb') as file:
        file.write(requests.get(uri, timeout=10).content)

    # Rename (remove wildcard characters)
    src = f  # original name
    for c in ['%20', '%', '*', '~', '(', ')']:
        f = f.replace(c, '_')
    f = f[:f.index('?')] if '?' in f else f  # new name
    if src != f:
        os.rename(src, f)  # rename

    # Add suffix (if missing)
    if Path(f).suffix == '':
        src = f  # original name
        f += '.' + Image.open(f).format.lower()  # append PIL format
        os.rename(src, f)  # rename
