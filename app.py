from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# هادي اللي ناقصة ❗
@app.route("/products")
def products():
    data = ["PC Gamer", "iPhone", "Keyboard"]
    return jsonify(data)

if __name__ == "__main__":
    app.run()