from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# API ديال products
@app.route("/products")
def products():
    data = [
        {"name": "PC Gamer", "url": "https://www.google.com"},
        {"name": "iPhone", "url": "https://www.apple.com"},
        {"name": "Keyboard", "url": "https://www.amazon.com"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run()