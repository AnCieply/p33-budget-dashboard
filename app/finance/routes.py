from flask import render_template, session, redirect, url_for, request
from json import loads

from app.finance import bp
from app.models.user_data import *


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
        category = request.form["Categories"]
        amount = request.form["Amount"]
        
        # If no option was chosen for Pos
        if "Pos" not in request.form:
            return redirect(url_for("finance.create_trans_page"))
        
        pos = request.form["Pos"]
        
        # If any field was left blank
        if account == "" or date == "" or category == "" or amount == "":
            return redirect(url_for("finance.create_trans_page"))
        
        true_amount = 0
        if pos == "+":
            pos = True
            modify_user_balance(id, float(amount))
        else:
            pos = False
            true_amount = float(amount)
            modify_user_balance(id, -true_amount)
        
        add_user_transaction(id, account, date, category, amount, pos)
        
        increment_category_trans(id, category)
        modify_category_spent(id, category, true_amount)
        
    categories = get_budget_categories(id)
    return render_template("finance/createtransaction.html", categories=categories)


@bp.route("/spendingplan", methods=["POST", "GET"])
def spending_plan_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    
    categories = get_budget_categories(id)
    return render_template("finance/spendingplan.html", page="spending", categories=categories)


@bp.route("/spendingplan/createcategory", methods=["POST", "GET"])
def create_category_page():
    id = session.get("id")
    # Send back to login page if no account logged in
    if id is None:
        return redirect(url_for("access.signin_page"))
    
    if request.method == "POST":
        name = request.form["Name"]
        amount = request.form["SpendingLimit"]
        
        # If any field was left blank
        if name == "" or amount == "":
            return redirect(url_for("finance.create_category_page"))
        
        create_budget_category(id, name, float(amount))
    
    return render_template("finance/createcategory.html")

