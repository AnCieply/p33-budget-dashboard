from flask import render_template, session, request, url_for, redirect
from sqlalchemy import select
import json

from init import app, db
from models.dashboard_model import get_user_balance, register_transaction, get_transactions, modify_user_balance
from models.db_models import UserData

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect("/login")
    # Arcane code that formats the float value as dollars and cents
    balance = "${:,.2f}".format(get_user_balance(int(id or 0)))
    return render_template("dashboard.html", page="dash", id=id, balance=balance, transactions=get_transactions(id))

@app.route("/createtransaction", methods=["POST", "GET"])
def create_trans_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect("/login")
    
    if request.method == "POST":
        account = request.form["Account"]
        date = request.form["Date"]
        category = request.form["Category"]
        amount = request.form["Amount"]
        pos = request.form["Pos"]
        
        if pos == "+":
            pos = True
            modify_user_balance(id, float(amount))
        else:
            pos = False
            modify_user_balance(id, -float(amount))
        
        register_transaction(id, account, date, category, amount, pos)
        
    
    return render_template("createtransaction.html")