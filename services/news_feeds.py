import feedparser
import requests
from services.feed_utils import get_og_image, extract_image_from_summary
from services.flex_builder import create_bubble

def generate_feed_bubbles(url, extract_func):
    try:
        feed = feedparser.parse(requests.get(url, timeout=5).text)
    except:
        return []
    return [create_bubble(e.title, e.link, extract_func(e)) for e in feed.entries[:5]]

def generate_it_news_bubbles():
    return generate_feed_bubbles("https://gigazine.net/news/rss_2.0/", lambda e: get_og_image(e.link))

def generate_business_bubbles():
    return generate_feed_bubbles("https://business.nikkei.com/rss/", lambda e: get_og_image(e.link))

def generate_entertainment_bubbles():
    return generate_feed_bubbles("https://eiga.com/rss/news/", lambda e: get_og_image(e.link))

def generate_education_bubbles():
    return generate_feed_bubbles("https://www.nhk.or.jp/school/rss/index.xml", lambda e: get_og_image(e.link))

def generate_real_estate_bubbles():
    return generate_feed_bubbles("https://suumo.jp/journal/feed/", lambda e: extract_image_from_summary(e.get("summary", "")))

def generate_game_bubbles():
    return generate_feed_bubbles("https://www.4gamer.net/rss/index.xml", lambda e: get_og_image(e.link))

def generate_world_news_bubbles():
    return generate_feed_bubbles("https://www3.nhk.or.jp/rss/news/cat0.xml", lambda e: get_og_image(e.link))
