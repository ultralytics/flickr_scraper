import glob
import os
from multiprocessing.pool import ThreadPool

import numpy as np
from skimage import io, transform  # conda install -c conda-forge scikit-image
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
            img = io.imread(f)

            # Downsize to max_wh if necessary
            r = max_wh / max(img.shape)  # ratio
            if r < 1:  # resize
                print('Resizing %s' % f)
                img = transform.resize(img, (round(img.shape[0] * r), round(img.shape[1] * r)))
                io.imsave(f, img.astype(np.uint8))

            # Get hash for duplicate detection
            img = np.repeat(img[:, :, None], 3, axis=2) if len(img.shape) == 2 else img  # greyscale to rgb
            img = img[:, :, :3] if img.shape[2] == 4 else img  # rgba to rgb (for pngs)
            hash = list(img.reshape(-1, 3).mean(0)) + list(img.reshape(-1, 3).std(0))  # unique to each image
            return [f, hash]

        # Remove corrupted
        except:
            print('Corrupted image: %s' % f)
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
                    os.remove(f[j]) if remove else None
                print('Duplicate images %s %s' % (f[i], [f[j] for j in duplicates]))
    print('Found %g duplicates.' % len(removed))


if __name__ == '__main__':
    files = sorted(glob.iglob('images/**/*.*', recursive=True))
    assert len(files), 'No files found'
    scan(files, max_wh=2000, remove=True, multi_thread=True)
