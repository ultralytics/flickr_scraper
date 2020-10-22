import glob
import os
from multiprocessing.pool import ThreadPool

import numpy as np
from PIL import Image
from tqdm import tqdm


def scan(files, max_wh=2000, remove=False, multi_thread=True):  # filelist, maximum image wh, remove corrupted/duplicate

    def scan_one_file(f):
        # Remove bad suffixes
        suffix = f.split('.')[-1]
        if suffix in ['gif', 'svg', 'ico']:  # bad suffix list
            print('Bad suffix %s' % f)
            os.remove(f) if remove else None
            return None

        # Downsize
        try:
            img = Image.open(f)

            # Checks (from YOLOv5)
            img.verify()  # PIL verify
            assert min(img.size) > 9, 'image size <10 pixels'

            # Downsize to max_wh if necessary
            r = max_wh / max(img.size)  # ratio (width, height = img.size)
            if r < 1:  # resize
                print('Resizing %s' % f)
                img = img.resize((round(x * r) for x in img.size), Image.ANTIALIAS)  # resize(width, height)

            # Resave
            img.save(f)

            # Get hash for duplicate detection
            img = np.array(img)  # to numpy
            img = np.repeat(img[:, :, None], 3, axis=2) if len(img.shape) == 2 else img  # greyscale to rgb
            img = img[:, :, :3] if img.shape[2] == 4 else img  # rgba to rgb (for pngs)
            hash = list(img.reshape(-1, 3).mean(0)) + list(img.reshape(-1, 3).std(0))  # unique to each image
            return [f, hash]

        # Remove corrupted
        except Exception as e:
            print('WARNING: %s: %s' % (f, e))
            os.remove(f) if remove else None
            return None

    # Scan all images
    a = []  # list of good filenames, hashes
    nf = len(files)
    if multi_thread:
        results = ThreadPool(20).imap_unordered(scan_one_file, files)  # 20 threads
        for r in tqdm(results, desc='Scanning images', total=nf):
            a.append(r) if r else None
    else:  # single-thread
        for f in tqdm(files, desc='Scanning images', total=nf):
            r = scan_one_file(f)
            a.append(r) if r else None

    # Remove duplicates
    f, x = list(zip(*a))  # files, hashes
    x = np.array(x)
    thres = 0.5  # threshold for declaring images identical (tunable parameter)
    removed = []  # removed items
    for i in range(len(f)):
        if i not in removed:  # if not removed
            duplicates = list(
                (((x[i] - x) ** 2).sum(1) < thres).nonzero()[0])  # list of duplicate images (including self)
            duplicates.remove(i)  # remove self from duplicate list
            if any(duplicates):
                for j in duplicates:
                    removed.append(j)
                    if remove and os.path.exists(f[j]):
                        os.remove(f[j])
                print('Duplicate images %s %s' % (f[i], [f[j] for j in duplicates]))
    print('Found %g duplicates.' % len(removed))


if __name__ == '__main__':
    files = sorted(glob.iglob('../images/**/*.*', recursive=True))
    assert len(files), 'No files found'
    scan(files, max_wh=2000, remove=True, multi_thread=True)
