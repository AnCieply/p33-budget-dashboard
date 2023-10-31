from flask import render_template, session, redirect, url_for, request
from json import loads

from app.finance import bp
from app.models.user_data import get_user_balance, modify_user_balance, add_user_transaction, get_user_data


@bp.route("/")
def index():
    return render_template("finance/index.html")


@bp.route("/dashboard", methods=["POST", "GET"])
def dashboard_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    # Arcane code that formats the float value as dollars and cents
    balance = "${:,.2f}".format(get_user_balance(int(id or 0)))
    return render_template("finance/dashboard.html", page="dash", id=id, balance=balance, transactions=loads(get_user_data(id).transactions))


@bp.route("/dashboard/createtransaction", methods=["POST", "GET"])
def create_trans_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    
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
        
        add_user_transaction(id, account, date, category, amount, pos)
        
    
    return render_template("finance/createtransaction.html")


@bp.route("/report", methods=["POST", "GET"])
def report_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    return render_template("finance/report.html", page="report")


@bp.route("/spendingplan", methods=["POST", "GET"])
def spending_plan_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    return render_template("finance/spendingplan.html", page="spending")

