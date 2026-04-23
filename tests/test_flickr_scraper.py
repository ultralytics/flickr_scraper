# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

import pytest

import flickr_scraper
from utils.general import download_uri, safe_filename_from_uri


def test_build_photo_url_prefers_original_url():
    """Ensure original Flickr URLs are preferred when present."""
    photo = {
        "url_o": "https://live.staticflickr.com/photo_o.jpg",
        "farm": "1",
        "server": "2",
        "id": "3",
        "secret": "4",
    }

    assert flickr_scraper.build_photo_url(photo) == "https://live.staticflickr.com/photo_o.jpg"


def test_build_photo_url_skips_photos_without_original_url():
    """Ensure secret-bearing fallback URLs are not built."""
    photo = {"farm": "1", "server": "2", "id": "3", "secret": "4"}

    assert flickr_scraper.build_photo_url(photo) is None


def test_resolve_credentials_requires_key_and_secret(monkeypatch):
    """Ensure missing Flickr credentials fail before making API requests."""
    monkeypatch.delenv("FLICKR_API_KEY", raising=False)
    monkeypatch.delenv("FLICKR_API_SECRET", raising=False)
    monkeypatch.setattr(flickr_scraper, "key", "")
    monkeypatch.setattr(flickr_scraper, "secret", "")

    with pytest.raises(ValueError, match="Flickr API key and secret are required"):
        flickr_scraper.resolve_credentials()


def test_get_urls_uses_json_search_and_redacts_output(monkeypatch, capsys):
    """Ensure get_urls uses photos.search, skips secret fallback URLs, and redacts output."""
    calls = []

    class FakePhotos:
        def search(self, **kwargs):
            calls.append(kwargs)
            return {
                "photos": {
                    "page": 3,
                    "pages": 10,
                    "photo": [
                        {"url_o": "https://example.com/1.jpg"},
                        {"farm": "1", "server": "2", "id": "3", "secret": "4"},
                        {"url_o": "https://example.com/extra.jpg"},
                    ],
                },
                "stat": "ok",
            }

    class FakeFlickr:
        def __init__(self, api_key, api_secret, format):
            self.api_key = api_key
            self.api_secret = api_secret
            self.format = format
            self.photos = FakePhotos()

    monkeypatch.setattr(flickr_scraper, "FlickrAPI", FakeFlickr)

    urls = flickr_scraper.get_urls("bees", n=2, api_key="key", api_secret="secret", page=3)
    stdout = capsys.readouterr().out

    assert urls == ["https://example.com/1.jpg", "https://example.com/extra.jpg"]
    assert "https://example.com" not in stdout
    assert "3_4_b.jpg" not in stdout
    assert "skipped (missing original URL)" in stdout
    assert calls == [
        {
            "text": "bees",
            "extras": "url_o",
            "per_page": 2,
            "page": 3,
            "license": "",
            "media": "photos",
            "sort": "relevance",
        }
    ]


def test_get_urls_raises_flickr_api_errors(monkeypatch):
    """Ensure Flickr API failures surface actionable errors."""

    class FakePhotos:
        def search(self, **kwargs):
            return {"stat": "fail", "code": 500, "message": "Internal Server Error"}

    class FakeFlickr:
        def __init__(self, api_key, api_secret, format):
            self.photos = FakePhotos()

    monkeypatch.setattr(flickr_scraper, "FlickrAPI", FakeFlickr)

    with pytest.raises(RuntimeError, match="Flickr API error 500: Internal Server Error"):
        flickr_scraper.get_urls("bees", n=1, api_key="key", api_secret="secret")


def test_get_urls_wraps_flickr_request_exceptions(monkeypatch):
    """Ensure Flickr request exceptions are reported without traceback-only output."""

    class FakePhotos:
        def search(self, **kwargs):
            raise ConnectionError("Status code 500 received")

    class FakeFlickr:
        def __init__(self, api_key, api_secret, format):
            self.photos = FakePhotos()

    monkeypatch.setattr(flickr_scraper, "FlickrAPI", FakeFlickr)

    with pytest.raises(RuntimeError, match="Flickr API request failed: Status code 500 received"):
        flickr_scraper.get_urls("bees", n=1, api_key="key", api_secret="secret")


def test_download_uri_joins_directory_and_sanitizes_filename(monkeypatch, tmp_path):
    """Ensure downloads are written inside the target directory with sanitized names."""

    class Response:
        content = b"image"

        def raise_for_status(self):
            pass

    monkeypatch.setattr("utils.general.requests.get", lambda *args, **kwargs: Response())

    download_uri("https://example.com/folder/photo%20name(1).jpg?size=o", tmp_path)

    assert (Path(tmp_path) / "photo_name_1_.jpg").read_bytes() == b"image"


def test_safe_filename_from_uri_removes_query_parameters():
    """Ensure query parameters are not persisted in temporary filenames."""
    uri = "https://example.com/folder/photo name.jpg?secret=token&download=1"

    assert safe_filename_from_uri(uri) == "photo_name.jpg"
