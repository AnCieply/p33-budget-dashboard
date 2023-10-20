from flask import render_template, request, url_for, redirect

from init import app
from models.dashboard_model import get_user_balance

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard_page():
    id = request.cookies.get("id", -1, type=int)
    # Send back to login page if no account logged in
    if id == -1:
        return redirect("/login")
    # Arcane code that formats the float value as dollars and cents
    balance = "${:,.2f}".format(get_user_balance(int(id or 0)))
    return render_template("dashboard.html", page="dash", id=id, balance=balance)
