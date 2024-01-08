<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🚀 Introduction

Flickr scraper is a Python tool designed to help you gather images from Flickr to create datasets for YOLO training. Given your search criteria, this tool simplifies the process of collecting relevant images for various computer vision tasks.

[![Ultralytics Actions](https://github.com/ultralytics/flickr_scraper/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/flickr_scraper/actions/workflows/format.yml)

## 🌟 Key Features

- Search image on Flickr using keywords.
- Download images directly for dataset assembly.
- Streamline the process of collecting training data for YOLO models.

# 🔧 Requirements

Ensure you have Python 3.7 or later installed. The required dependencies can be installed using:

```bash
pip install -U -r requirements.txt
```

Key packages include:

- `flickrapi`

# 🛠 Install

To set up the Flickr scraper, follow these steps:

```bash
git clone https://github.com/ultralytics/flickr_scraper
cd flickr_scraper
pip install -U -r requirements.txt
```

# ⚙️ Run

Before you begin:

1. Obtain a Flickr API key [here](https://www.flickr.com/services/apps/create/apply).

2. Insert your API key and secret into `flickr_scraper.py`:

```python
# Replace with your Flickr API key and secret
key = 'YOUR_API_KEY'
secret = 'YOUR_API_SECRET'
```

3. Execute the script with your search criteria. Specify the number of images to fetch (`--n`) and use `--download` to save the images locally. Downloaded images are saved to `flickr_scraper/images`. Keep in mind Flickr's rate limits and terms of use. Learn more from the [Flickr API documentation](https://www.flickr.com/services/developer/api/).

Example command:

```bash
python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download
```

You will see output similar to:

```plaintext
0/10 https://live.staticflickr.com/21/38596887_40df118fd9_o.jpg
...
9/10 https://live.staticflickr.com/1770/43276172331_e779b8c161_o.jpg
Done. (4.1s)
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```

Images are then available in the specified folder, ready for further processing or training.

<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="">

# 📜 Cite

If our project assists in your research or work, please consider citing it:

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

# 🤝 Contribute

We welcome contributions from the community! Whether you're fixing bugs, adding new features, or improving documentation, your input is invaluable. Take a look at our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started. Also, we'd love to hear about your experience with Ultralytics products. Please consider filling out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge 🙏 and thank you to all of our contributors!

<!-- Ultralytics contributors -->

<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

# ©️ License

Ultralytics is excited to offer two different licensing options to meet your needs:

- **AGPL-3.0 License**: Perfect for students and hobbyists, this [OSI-approved](https://opensource.org/licenses/) open-source license encourages collaborative learning and knowledge sharing. Please refer to the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for detailed terms.
- **Enterprise License**: Ideal for commercial use, this license allows for the integration of Ultralytics software and AI models into commercial products without the open-source requirements of AGPL-3.0. For use cases that involve commercial applications, please contact us via [Ultralytics Licensing](https://ultralytics.com/license).

# 📬 Contact Us

For bug reports, feature requests, and contributions, head to [GitHub Issues](https://github.com/ultralytics/flickr_scraper/issues). For questions and discussions about this project and other Ultralytics endeavors, join us on [Discord](https://ultralytics.com/discord)!

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
