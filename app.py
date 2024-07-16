from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", is_index=True)


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html", is_index=False)


@app.route("/coupons")
def coupons():
    return render_template("coupons.html", is_index=False)


@app.route("/location")
def location():
    return render_template("location.html", is_index=False)


@app.route("/services")
def services():
    return render_template("services.html", is_index=False)


@app.route("/news")
def news():
    return render_template("news.html", is_index=False)


@app.route("/removed")
def removed():
    return render_template("index-removed.html", is_index=False)


if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", "8080"))
    app.run(debug=True, port=server_port, host="0.0.0.0")
