<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# Introduction

Flickr scraper assists in compiling images for YOLO training from Flickr based on user input search criteria. This is helpful for quickly creating a dataset for computer vision tasks.

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

# Contribute

We love your input! Ultralytics open-source efforts would not be possible without help from our community. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started, and fill out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) to send us feedback on your experience. Thank you 🙏 to all our contributors!

<!-- SVG image from https://opencollective.com/ultralytics/contributors.svg?width=990 -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

# License

Ultralytics offers two licensing options to accommodate diverse use cases:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/licenses/) open-source license is ideal for students and enthusiasts, promoting open collaboration and knowledge sharing. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for more details.
- **Enterprise License**: Designed for commercial use, this license permits seamless integration of Ultralytics software and AI models into commercial goods and services, bypassing the open-source requirements of AGPL-3.0. If your scenario involves embedding our solutions into a commercial offering, reach out through [Ultralytics Licensing](https://ultralytics.com/license).

# Contact

For Ultralytics bug reports and feature requests please visit [GitHub Issues](https://github.com/ultralytics/flickr_scraper/issues), and join our [Discord](https://ultralytics.com/discord) community for questions and discussions!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>

**Issues should be raised directly in the repository.** For business inquiries or professional support requests please visit https://www.ultralytics.com or email Glenn Jocher at glenn.jocher@ultralytics.com. 
