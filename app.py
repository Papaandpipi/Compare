from flask import Flask, redirect, render_template, request
from helpers import compare

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        text1 = request.form.get("text1")
        text2 = request.form.get("text2")

        #TODO call compare function from helpers

        #s1 = "This is a very cold hot summer. How are you? I am no."
        #s2 = "This is mildly cold winter. What are you? You are yes."
        
        result = compare(text1, text2)

        return render_template("index.html", result = result)

    else:

        return render_template("index.html")