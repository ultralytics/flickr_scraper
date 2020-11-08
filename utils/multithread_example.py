#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer
from urllib import request

from tqdm import tqdm

dir = '../'  # directory to save image downloads
urls = ['https://farm8.staticflickr.com/7428/27138770446_6618c10ffb_b.jpg',
        'https://live.staticflickr.com/4571/37795143414_8ccae77768_o.jpg',
        'https://live.staticflickr.com/1732/27535176747_78b83536af_o.jpg',
        'https://live.staticflickr.com/331/18765122504_ea8c9ea6ce_o.jpg',
        'https://live.staticflickr.com/1919/44312457665_6f7b6c2c42_o.jpg',
        'https://farm4.staticflickr.com/3597/3359921429_fc86a7519e_b.jpg'] * 10


def fetch_url(url):
    try:
        f = dir + url.split('/')[-1]
        request.urlretrieve(url, f)
        return url, ''
    except Exception as e:
        return url, e


# Multi-thread
t = timer()
results = ThreadPool(8).imap_unordered(fetch_url, urls)  # 8 threads
pbar = tqdm(enumerate(results), total=len(urls))
for i, (url, resp) in pbar:
    pbar.desc = '%g %r %s' % (i, url, resp)
print('Done multi-thread (%.2fs)\n' % (timer() - t))

# Single-thread
t = timer()
pbar = tqdm(range(len(urls)))
for i in pbar:
    url, resp = fetch_url(urls[i])
    pbar.desc = '%g %r %s' % (i, url, resp)
print('Done single-thread (%.2fs)\n' % (timer() - t))
