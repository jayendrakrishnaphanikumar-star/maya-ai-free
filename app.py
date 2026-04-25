@app.route("/")
def home():
    return "Maya AI is running!"
    from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
