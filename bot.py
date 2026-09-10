import os
from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__, static_folder='.')

TOKEN = "8624429601:AAEap1H0wsyUpTrzEPWPpFkSa-VOtq_RfpY"

@app.route("/", methods=["GET"])
def home():
    return "Bot status: Active", 200

@app.route("/index.html", methods=["GET"])
def webapp():
    return send_from_directory('.', 'index.html')

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        
        host_url = request.host_url.rstrip('/')
        webapp_url = f"{host_url}/index.html"
        
        payload = {
            "chat_id": chat_id,
            "text": "Xush kelibsiz! WebApp tugmasi tayyor:",
            "reply_markup": {
                "inline_keyboard": [[
                    {"text": "🚀 WebApp-ni ochish", "web_app": {"url": webapp_url}}
                ]]
            }
        }
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json=payload)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
