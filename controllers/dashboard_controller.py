from flask import render_template, request, url_for

from init import app
from models.dashboard_model import get_user_balance

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard_page():
    id = request.cookies.get("id")
    balance = get_user_balance(int(id or 0))
    return render_template("dashboard.html", id=id, balance=balance)
