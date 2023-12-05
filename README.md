<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🚀 Introduction

Flickr scraper is a Python tool designed to help you gather images from Flickr to create datasets for YOLO training. Given your search criteria, this tool simplifies the process of collecting relevant images for various computer vision tasks.

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

Your contributions make the open-source community richer. Whether it's a bug fix, new feature, or additional documentation, we deeply appreciate your efforts.

👉 Check out our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to start contributing and complete our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) to share your user experience. A massive thank you 🙏 to everyone involved!

<!-- Show appreciation to our contributors with an image link -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
    <img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors">
</a>

# 📄 License

Ultralytics software is dual-licensed under:

- **AGPL-3.0 License**: This [Open Source Initiative](https://opensource.org/licenses/) approved license is suitable for students, researchers, and hobbyists for open collaboration. Refer to the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for details.
- **Commercial Use**: For embedding Ultralytics software in commercial products, consider our Enterprise License for a permission-based use without the stipulations of AGPL-3.0.

# 📞 Contact

Need assistance or want to provide feedback? Here's how you can reach us:

- Bug reports and feature requests: Submit through [GitHub Issues](https://github.com/ultralytics/flickr_scraper/issues).
- Join the conversation: Connect with our community on [Discord](https://ultralytics.com/discord).
- Professional inquiries: Visit us at https://www.ultralytics.com for business-related queries.

<br>
<div align="center">
  <!-- Linking Ultralytics social media and related pages with icons -->
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>

<!-- Guideline for users on how to reach out for different types of queries -->
**Please direct all questions regarding use and support to our [Discord](https://ultralytics.com/discord) community, and reserve GitHub Issues for bug reports and feature requests.** For official business inquiries or professional support, please visit our website or reach out through our social media channels.
