 <img src="https://storage.googleapis.com/ultralytics/logo/logoname1000.png" width="160">

# Introduction

This directory contains Flickr image-scraping software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

# Requirements

Python 3.7 or later with all of the `pip install -U -r requirements.txt` packages including:
- `flickrapi`

# Install
```bash
$ git clone https://github.com/ultralytics/flickr_scraper
$ cd flickr_scraper
$ pip install -U -r requirements.txt
```

# Run

1. Request a Flickr API key: https://www.flickr.com/services/apps/create/apply

2. Write your API key and secret in `flickr_scraper.py` L11-L12:
```python
key = ''
secret = ''
```

3. Search for up to `n` images, and optionally `--download`. URLs are printed to screen and downloaded images are saved in `flickr_scraper/images`. Note that image downloads may be subject to Flickr rate limits and other limitations. See https://www.flickr.com/services/developer/api/ for full information.

```bash
$ python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download

0/10 https://live.staticflickr.com/21/38596887_40df118fd9_o.jpg
1/10 https://live.staticflickr.com/4800/40729137901_5dafdc039f_o.jpg
2/10 https://farm8.staticflickr.com/7428/27138770446_6618c10ffb_b.jpg
3/10 https://live.staticflickr.com/925/29647053658_728134f6ca_o.jpg
4/10 https://live.staticflickr.com/1732/27535176747_78b83536af_o.jpg
5/10 https://live.staticflickr.com/7850/47160160332_6b0c88e207_o.jpg
6/10 https://live.staticflickr.com/1919/44312457665_6f7b6c2c42_o.jpg
7/10 https://live.staticflickr.com/7922/46297818725_21c13a3629_o.jpg
8/10 https://live.staticflickr.com/8045/29760999676_e71c938283_o.jpg
9/10 https://live.staticflickr.com/1770/43276172331_e779b8c161_o.jpg
Done. (4.1s)
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```
<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="">

# Cite

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

## About Us

Ultralytics is a U.S.-based particle physics and AI startup with over 6 years of expertise supporting government, academic and business clients. We offer a wide range of vision AI services, spanning from simple expert advice up to delivery of fully customized, end-to-end production solutions, including:
- **Cloud-based AI** systems operating on **hundreds of HD video streams in realtime.**
- **Edge AI** integrated into custom iOS and Android apps for realtime **30 FPS video inference.**
- **Custom data training**, hyperparameter evolution, and model exportation to any destination.

For business inquiries and professional support requests please visit us at https://www.ultralytics.com. 


## Contact

**Issues should be raised directly in the repository.** For business inquiries or professional support requests please visit https://www.ultralytics.com or email Glenn Jocher at glenn.jocher@ultralytics.com. 
