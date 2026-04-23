from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def ask_maya(message):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        return response.json()[0]["generated_text"]
    except:
        return "Maya is thinking... try again"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    reply = ask_maya(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()