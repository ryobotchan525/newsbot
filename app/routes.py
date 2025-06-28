from flask import request
from threading import Thread
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    PostbackEvent, FlexSendMessage
)

from app import app, line_bot_api, handler
from services.news_feeds import *
from services.flex_builder import send_genre_flex

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    def process():
        try:
            handler.handle(body, signature)
        except Exception as e:
            print(f"Webhook Error: {e}")

    Thread(target=process).start()
    return "OK", 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    send_genre_flex(event.source.user_id)

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    user_id = event.source.user_id

    genre_mapping = {
        "genre=it": (generate_it_news_bubbles, "💻 ITニュース！"),
        "genre=business": (generate_business_bubbles, "📈 ビジネスニュース！"),
        "genre=education": (generate_education_bubbles, "📚 教育ニュース！"),
        "genre=game": (generate_game_bubbles, "🎮 ゲームニュース！"),
        "genre=entertainment": (generate_entertainment_bubbles, "🎬 エンタメニュース！"),
        "genre=real_estate": (generate_real_estate_bubbles, "🏠 不動産ニュース！"),
        "genre=world": (generate_world_news_bubbles, "🌍 海外ニュース！")
    }

    if data in genre_mapping:
        generate_func, alt_text = genre_mapping[data]
        bubbles = generate_func()

        if not bubbles:
            line_bot_api.push_message(user_id, TextSendMessage(text="⚠️ ニュースが取得できませんでした"))
            return

        carousel = {"type": "carousel", "contents": bubbles}
        line_bot_api.push_message(user_id, FlexSendMessage(alt_text=alt_text, contents=carousel))
    else:
        line_bot_api.push_message(user_id, TextSendMessage(text="⚠️ 不明なジャンルが選択されました。"))
