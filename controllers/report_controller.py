from flask import render_template, url_for, request, redirect

from init import app

@app.route("/report", methods=["POST", "GET"])
def report_page():
    id = request.cookies.get("id", -1, type=int)
    # Send back to login page if no account logged in
    if id == -1:
        return redirect("/login")
    return render_template("report.html", page="report")
