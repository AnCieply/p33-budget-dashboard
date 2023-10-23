from flask import render_template, session, url_for, request, redirect

from init import app

@app.route("/report", methods=["POST", "GET"])
def report_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect("/login")
    return render_template("report.html", page="report")
