# /app.py

import os
import requests
import urllib.parse
from dotenv import load_dotenv
from pathlib import Path
import argparse
import yaml

def load_config():
    config = {}
    if os.path.exists('config.local.yaml'):
        with open('config.local.yaml', 'r') as f:
            config.update(yaml.safe_load(f))
    elif os.path.exists('config.default.yaml'):
        with open('config.default.yaml', 'r') as f:
            config.update(yaml.safe_load(f))
    return config

def create_output_folder(folder_name):
    Path(folder_name).mkdir(parents=True, exist_ok=True)

def search_flickr(api_key, search_phrase, per_page=100, page=1):
    base_url = "https://api.flickr.com/services/rest/"
    params = {
        "method": "flickr.photos.search",
        "api_key": api_key,
        "format": "json",
        "nojsoncallback": 1,
        "text": search_phrase,
        "per_page": per_page,
        "page": page,
        "sort": "relevance",
        "extras": "url_o"
    }
    response = requests.get(base_url, params=params)
    return response.json()

def download_image(url, folder, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(response.content)

def main(search_phrase, output_folder):
    load_dotenv()
    config = load_config()

    api_key = os.getenv("FLICKR_API_KEY") or config.get("FLICKR_API_KEY")
    api_secret = os.getenv("FLICKR_API_SECRET") or config.get("FLICKR_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Flickr API key and secret are required.")

    create_output_folder(output_folder)

    search_variations = [
        search_phrase,
        search_phrase.replace(" ", "_"),
        search_phrase.replace(" ", "-")
    ]
    combined_search = " OR ".join(f'"{variation}"' for variation in search_variations)

    page = 1
    while True:
        result = search_flickr(api_key, combined_search, page=page)
        if "photos" not in result or "photo" not in result["photos"]:
            break

        photos = result["photos"]["photo"]
        if not photos:
            break

        for photo in photos:
            if "url_o" in photo:
                filename = f"{photo['id']}.jpg"
                download_image(photo["url_o"], output_folder, filename)

        page += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from Flickr based on a search phrase.")
    parser.add_argument("search_phrase", help="The phrase to search for on Flickr")
    parser.add_argument("--output", default="output", help="Output folder for downloaded images")
    args = parser.parse_args()

    main(args.search_phrase, args.output)
