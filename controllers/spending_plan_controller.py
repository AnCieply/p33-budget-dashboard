from flask import render_template, url_for

from init import app

@app.route("/spendingplan", methods=["POST", "GET"])
def spending_plan_page():
    return render_template("spendingplan.html", page="spending")
