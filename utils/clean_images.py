import argparse
import glob
import os
from multiprocessing.pool import ThreadPool
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm


def scan(files, max_wh=1920, remove=False, multi_thread=True, tojpg=False, quality=95, workers=8):
    # Args:
    #   files: list of image files
    #   max_wh: maximum image wh (larger images will be reduced in size)
    #   remove: delete corrupted/duplicate images
    #   tojpg: replace current image with jpg for smaller size / faster loading
    #   quality: PIL JPG saving quality (0-100)
    img_formats = ['.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.dng']  # valid image formats from YOLOv5

    def scan_one_file(f):
        try:
            # Rename (remove wildcard characters)
            src = f  # original name
            for s in ['%20', '%', '*', '~', '(', ')']:  # strings to remove
                f = f.replace(s, '_')
            f = f[:f.index('?')] if ('?' in f and os.sep + '?' not in f) else f  # remove after '?' char
            if src != f:
                os.rename(src, f)  # rename

            # Add suffix (if missing)
            if Path(f).suffix == '':
                src = f  # original name
                f += '.' + Image.open(f).format.lower()  # append PIL format
                os.rename(src, f)  # rename

            # Check suffix
            if Path(f).suffix.lower() not in img_formats:
                print('Invalid suffix %s' % f)
                os.remove(f) if remove else None
                return None

            # Check image
            Image.open(f).verify()  # PIL verify
            img = Image.fromarray(cv2.imread(f)[:, :, ::-1])  # cv2 to PIL for 4ch PNGs and 1ch greyscale to 3ch
            assert min(img.size) > 9, 'image size <10 pixels'

            # Downsize
            r = max_wh / max(img.size)  # ratio (width, height = img.size)
            if r < 1:  # resize
                print('Resizing %s' % f)
                img = img.resize((round(x * r) for x in img.size), Image.ANTIALIAS)  # resize(width, height)

            # Resave
            if tojpg:  # convert to JPG
                if os.path.exists(f):
                    os.remove(f)  # remove old
                f = f.replace(Path(f).suffix, '.jpg')
            img.save(f, quality=quality)

            # Hash for duplicate detection
            img = np.array(img)  # to numpy
            img = np.repeat(img[:, :, None], 3, axis=2) if len(img.shape) == 2 else img  # greyscale to rgb
            img = img[:, :, :3] if img.shape[2] == 4 else img  # rgba to rgb (for pngs)
            hash = list(img.reshape(-1, 3).mean(0)) + list(img.reshape(-1, 3).std(0))  # unique to each image
            return [f, hash]

        # Remove corrupted
        except Exception as e:
            print('WARNING: %s: %s' % (f, e))
            if remove and os.path.exists(f):
                os.remove(f)
            return None

    # Scan all images
    a = []  # list of good filenames, hashes
    nf = len(files)
    if multi_thread:
        results = ThreadPool(workers).imap_unordered(scan_one_file, files)  # 8 threads
        for r in tqdm(results, desc='Scanning images', total=nf):
            a.append(r) if r else None
    else:  # single-thread
        for f in tqdm(files, desc='Scanning images', total=nf):
            r = scan_one_file(f)
            a.append(r) if r else None

    # Remove duplicates
    f, x = list(zip(*a))  # files, hashes
    x = np.array(x)
    thres = 0.2  # threshold for declaring images identical (tunable parameter)
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
    # python utils/clean_images.py --dir ../coco128/images --mawh 1024 --tojpg --workers 8
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='../images', help='image directory')
    parser.add_argument('--maxwh', type=int, default=1920, help='resize to down to --max_wh if larger')
    parser.add_argument('--remove', action='store_true', help='remove corrupted/duplicates')
    parser.add_argument('--tojpg', action='store_true', help='convert images to PIL JPG')
    parser.add_argument('--quality', type=int, default=95, help='JPG quality (0-100) if --tojpg')
    parser.add_argument('--workers', type=int, default=8, help='multi-thread workers')
    opt = parser.parse_args()

    dir = Path(opt.dir).resolve()
    files = sorted(glob.iglob(str(dir / '**/*.*'), recursive=True))
    assert len(files), f'No files found in {dir}'
    print(f'Cleaning {len(files)} images in {dir} ...')
    scan(files, max_wh=opt.maxwh, remove=opt.remove, tojpg=opt.tojpg, quality=opt.quality, workers=opt.workers)
    # zip -r data.zip data
