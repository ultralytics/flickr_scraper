<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🚀 Introduction

Welcome to the Flickr scraper project! This tool is designed to facilitate the acquisition of image data for machine learning tasks, specifically for those working with YOLO (You Only Look Once) models. By using simple search criteria provided by the user, it can quickly gather images from Flickr, streamlining the process of dataset creation for computer vision projects.

# 📋 Requirements

Ensure you have Python 3.7 or later installed on your system. Additionally, the necessary Python packages can be installed by running:

```bash
pip install -U -r requirements.txt
```

Among these, `flickrapi` is essential for accessing the Flickr API.

# 🔧 Installation

To set up the Flickr scraper on your local machine, follow these steps:

```bash
git clone https://github.com/ultralytics/flickr_scraper
cd flickr_scraper
pip install -U -r requirements.txt
```

# 🚦 Getting Started

Here's how to get your scraper up and running:

### 1. Obtain a Flickr API Key
First, request an API key from [Flickr](https://www.flickr.com/services/apps/create/apply).

### 2. Set Your API Credentials
Enter your API key and secret into `flickr_scraper.py` at the designated lines:

```python
# Enter your API key and secret here
key = 'YOUR_FLICKR_API_KEY'
secret = 'YOUR_FLICKR_API_SECRET'
```

### 3. Run the Scraper
To search for images and optionally download them, you can execute the following command. Downloaded images will be stored in `flickr_scraper/images`, and please bear in mind that image downloads are constrained by Flickr's rate limits and policies.

```bash
python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download
```

Example output showing image URLs (and image download if selected):
```
0/10 https://live.staticflickr.com/21/38596887_40df118fd9_o.jpg
...
9/10 https://live.staticflickr.com/1770/43276172331_e779b8c161_o.jpg
Done. (4.1s)
All images saved to /path/to/flickr_scraper/images/honeybees_on_flowers/
```

<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="">

# 📜 Citation

If you find this tool useful in your research, kindly cite it using the following:

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

# 🤝 Contributing

Your contributions are what make the community great. We welcome contributions from all skill levels and look forward to seeing your input. Check out our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to learn more about how you can get involved. Don’t forget to fill out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) to let us know about your user experience. A huge thank you 🙏 to all our amazing contributors!

<!-- Showcase of contributors -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

# 📄 License

Ultralytics offers two licensing options:

- **AGPL-3.0 License**: Grab a copy of our OSI-approved open-source license if you are a student, an enthusiast, or simply looking to collaborate and share knowledge. The full terms are available in the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file.
- **Enterprise License**: Designed for those looking to integrate this software into their commercial products, the Enterprise License offers seamless use of our tools and models without the open-source requirements of AGPL-3.0. For inquiries regarding this license, head to [Ultralytics Licensing](https://ultralytics.com/license).

# ✉️ Contact Information

Got a bug to report or an exciting feature to request? Feel free to open an [Issue on GitHub](https://github.com/ultralytics/flickr_scraper/issues). You can also join our lively [Discord community](https://ultralytics.com/discord) for discussions about the project.

<br>
<!-- Social media links -->
<div align="center">
  <!-- GitHub -->
  <a href="https://github.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- LinkedIn -->
  <a href="https://www.linkedin.com/company/ultralytics/">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- Twitter -->
  <a href="https://twitter.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- YouTube -->
  <a href="https://youtube.com/ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- TikTok -->
  <a href="https://www.tiktok.com/@ultralytics">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- Instagram -->
  <a href="https://www.instagram.com/ultralytics/">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram">
  </a>
  <!-- Spacer -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <!-- Discord -->
  <a href="https://ultralytics.com/discord">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord">
  </a>
</div>

**Please do not hesitate to report issues directly in the repository.** For professional support requests and business inquiries, visit our [website](https://www.ultralytics.com). 

**Please note:** Email support isn't available; hence direct email contacts have been omitted. We encourage the use of our public channels for support and queries to benefit the whole community.
