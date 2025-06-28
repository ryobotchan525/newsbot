import re
import requests
from bs4 import BeautifulSoup

DEFAULT_IMAGE_URL = "https://placehold.jp/600x400.png"

def get_og_image(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        tag = soup.find("meta", property="og:image")
        return tag["content"] if tag else DEFAULT_IMAGE_URL
    except:
        return DEFAULT_IMAGE_URL

def extract_image_from_summary(summary):
    match = re.search(r'<img[^>]+src="([^"]+)"', summary)
    return match.group(1) if match else DEFAULT_IMAGE_URL
