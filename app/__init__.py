from flask import Flask
from linebot import LineBotApi, WebhookHandler
import os

app = Flask(__name__)

LINE_CHANNEL_SECRET = os.getenv("YOUR_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("YOUR_CHANNEL_ACCESS_TOKEN")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
