from app import app
from flask import jsonify

@app.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Bot is alive!"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
