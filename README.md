<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Introduction

The Flickr Scraper is a [Python](https://www.python.org/) tool designed to help you gather images from [Flickr](https://www.flickr.com/) for creating custom datasets, particularly useful for [Ultralytics YOLO](https://docs.ultralytics.com/models/yolo11/) model training. Based on your search criteria, this tool simplifies the process of collecting relevant images for various [computer vision tasks](https://docs.ultralytics.com/tasks/), streamlining your [dataset preparation](https://docs.ultralytics.com/guides/data-collection-and-annotation/) workflow. Learn more about datasets in our blog post on the [best computer vision datasets](https://www.ultralytics.com/blog/exploring-the-best-computer-vision-datasets-in-2025).

[![Ultralytics Actions](https://github.com/ultralytics/flickr_scraper/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/flickr_scraper/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## 🌟 Key Features

- **Keyword Search**: Find images on Flickr using specific keywords relevant to your project.
- **Direct Download**: Easily download images to assemble your [computer vision](https://www.ultralytics.com/glossary/computer-vision-cv) [dataset](https://www.ultralytics.com/glossary/benchmark-dataset).
- **Streamlined Data Collection**: Simplify the process of gathering training data for [model training](https://docs.ultralytics.com/modes/train/) with YOLO models.

## 🔧 Requirements

Ensure you have Python 3.8 or later installed. The necessary dependencies can be installed using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -U -r requirements.txt
```

Key packages include:

- `flickrapi`: A Python wrapper for the Flickr API, essential for interacting with Flickr services. You can find more details on the [`flickrapi` PyPI page](https://pypi.org/project/flickrapi/).

## 🛠️ Installation

To set up the Flickr scraper on your local machine, follow these steps using [Git](https://git-scm.com/):

```bash
# Clone the repository
git clone https://github.com/ultralytics/flickr_scraper

# Navigate to the project directory
cd flickr_scraper

# Install the required packages
pip install -U -r requirements.txt
```

## ⚙️ Running the Scraper

Before you begin scraping images:

1.  **Get a Flickr API Key**: Obtain your unique API key and secret by applying [here](https://www.flickr.com/services/apps/create/apply).
2.  **Configure API Credentials**: Set your Flickr API key and secret as environment variables:

```bash
export FLICKR_API_KEY="YOUR_API_KEY"
export FLICKR_API_SECRET="YOUR_API_SECRET"
```

You can also pass credentials directly with `--key` and `--secret`, or insert them into `flickr_scraper.py` if you prefer a local-only script:

```python
# flickr_scraper.py
# Replace with your actual Flickr API key and secret
key = "YOUR_API_KEY"
secret = "YOUR_API_SECRET"
```

3.  **Execute the Script**: Run the script from your terminal, specifying your search query, the number of images to fetch (`--n`), and the `--download` flag to save them locally. Downloaded images are saved by default to the `flickr_scraper/images/` directory, organized into subfolders based on the search query.

    **Important**: Be mindful of Flickr's API rate limits and terms of service. Excessive requests may lead to temporary or permanent blocking. Refer to the official [Flickr API documentation](https://www.flickr.com/services/developer/api/) for detailed usage guidelines.

Example command to download 10 images matching 'honeybees on flowers':

```bash
python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download
```

You should see output indicating the download progress:

```plaintext
1/10 https://live.staticflickr.com/21/38596887_40df118fd9_o.jpg
...
10/10 https://live.staticflickr.com/1770/43276172331_e779b8c161_o.jpg
Done. (4.1s)
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```

The downloaded images will be available in the specified folder (e.g., `images/honeybees_on_flowers/`), ready for annotation, further processing, or direct use in training your models.

<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="600" alt="Example scraped image of a honeybee on a flower">

## 🔁 Downloading More Results

Flickr search order is controlled by the Flickr API and may change over time. If you run the same command again with the same search term, Flickr can return many of the same results. To continue from a later result page, use `--page`:

```bash
python3 flickr_scraper.py --search 'honeybees on flowers' --n 50 --download --page 2
```

The script de-duplicates URLs within each run, but it does not keep a persistent database of previously downloaded Flickr photo IDs. For repeat dataset collection, keep each search in its own folder and use `--page` to request later Flickr pages.

## 🧩 Compatibility Notes

This scraper uses Flickr's JSON `photos.search` API response directly. It does not call `flickrapi.walk()`, avoiding the older `getchildren()` compatibility error reported with `flickrapi==2.4.0` on Python 3.9 and newer.

If Flickr returns a `500` or another API error, the script reports the Flickr error code and message. These errors usually come from Flickr or invalid credentials; retry the command after checking your API key and secret.

## 📜 Citation

If the Flickr Scraper tool helps your research or work, please consider citing it using the following DOI:

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

## 🤝 Contributing

Contributions are welcome! We value input from the community to fix bugs, add features, or improve documentation. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for details on how to get started. Don't forget to share your experiences and feedback by completing our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). Thank you 🙏 to all our contributors!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## ©️ License

Ultralytics provides two licensing options for this project:

- **AGPL-3.0 License**: An [OSI-approved open-source license](https://opensource.org/license/agpl-v3), ideal for students and enthusiasts who wish to contribute and share improvements publicly. See the [LICENSE](https://github.com/ultralytics/flickr_scraper/blob/main/LICENSE) file for details.
- **Enterprise License**: Designed for commercial applications, this license allows for the integration of Ultralytics software and AI models into commercial products and services without the open-source requirements of AGPL-3.0. If your use case involves commercial deployment, please contact us through [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📬 Contact

For bug reports, feature suggestions, or contributions, please visit [GitHub Issues](https://github.com/ultralytics/flickr_scraper/issues). For broader questions and discussions about Ultralytics projects, join our active community on [Discord](https://discord.com/invite/ultralytics)! Explore the full range of our resources at [Ultralytics Docs](https://docs.ultralytics.com/).

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
