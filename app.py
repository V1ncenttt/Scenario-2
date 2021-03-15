from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect


app = Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/who_are_we")
def whoAreWe():
    return render_template("who_are_we.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/rien")
def rien():
    return "This part has not yet been implemented"

if __name__ == '__main__':
    app.run()