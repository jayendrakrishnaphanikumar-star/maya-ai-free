from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Maya AI is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Maya, a helpful AI assistant."},
                {"role": "user", "content": user_msg}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})
