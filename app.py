from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", is_index=True)


@app.route("/removed")
def removed():
    return render_template("index-removed.html", is_index=False)


if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", "8080"))
    app.run(debug=True, port=server_port, host="0.0.0.0")
