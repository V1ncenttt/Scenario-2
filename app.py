from flask import Flask, request
from flask.helpers import flash
from flask.templating import render_template
from operations import *


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

@app.route("/exercises")
def exercies():
    return render_template("exercises.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create", methods = ['POST', 'GET'])
def create():
    if request.method == "POST":
        data = request.form
        print(data)
    return render_template("create.html")

@app.route("/generator", methods = ['POST', 'GET'])
def generator():
    if request.method == "POST":
        data = request.form
        if (len(data["regex"]) > 0):
            try :
                nfa = regToNFA(data["regex"])
                writeDot(nfa)
                return render_template("generator.html", label = "Here is the output NFA", image = "static/Images/graph.png")
            except:
                return render_template("generator.html", label="Regex entered was not valid")
    return render_template("generator.html")




@app.route("/exercise-<exNum>")
def exercise(exNum):
    print(exNum)
    return render_template("index.html")

@app.route("/rien")
def rien():
    return "This part has not yet been implemented"

@app.errorhandler(404)
def pageNotFound(e):
    return "This page does not exist"

@app.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-store'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run()