from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are Maya, a helpful AI assistant."},
                {"role": "user", "content": user_msg}
            ]
        }

        res = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data
        )

        response = res.json()

        if "error" in response:
            return jsonify({"reply": str(response)})

        reply = response["choices"][0]["message"]["content"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})
