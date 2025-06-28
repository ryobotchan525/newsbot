from app import line_bot_api
from linebot.models import FlexSendMessage

def create_bubble(title, link, image_url):
    return {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": image_url,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "20:13"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
                {
                    "type": "text",
                    "text": title,
                    "weight": "bold",
                    "wrap": True,
                    "size": "md"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "続きを読む",
                        "uri": link
                    },
                    "style": "link"
                }
            ]
        }
    }

def send_genre_flex(user_id):
    def genre_bubble(title, label, data, emoji, color):
        return {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": f"https://placehold.jp/600x400.png?text={emoji}",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "1.51:1"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": title, "weight": "bold", "size": "lg"}
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": color,
                        "action": {
                            "type": "postback",
                            "label": label,
                            "data": data
                        }
                    }
                ]
            }
        }

    bubbles = [
        genre_bubble("IT", "ITニュース", "genre=it", "💻", "#2196F3"),
        genre_bubble("ビジネス", "ビジネス", "genre=business", "📈", "#4CAF50"),
        genre_bubble("エンタメ", "エンタメ", "genre=entertainment", "🎬", "#E91E63"),
        genre_bubble("不動産", "不動産", "genre=real_estate", "🏠", "#9C27B0"),
        genre_bubble("海外ニュース", "海外", "genre=world", "🌍", "#FF9800"),
        genre_bubble("ゲーム", "ゲーム", "genre=game", "🎮", "#795548"),
        genre_bubble("教育", "教育", "genre=education", "📚", "#3F51B5")
    ]

    message = FlexSendMessage(
        alt_text="ニュースジャンルを選んでね",
        contents={"type": "carousel", "contents": bubbles}
    )
    line_bot_api.push_message(user_id, message)
