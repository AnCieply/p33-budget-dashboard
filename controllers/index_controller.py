from flask import render_template

from init import app

# Index Controller
@app.route("/")
def index():
    return render_template("index.html")
