from flask import render_template, url_for

from init import app

@app.route("/report", methods=["POST", "GET"])
def report_page():
    return render_template("report.html", page="report")
