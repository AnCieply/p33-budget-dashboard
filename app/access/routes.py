from flask import render_template, session, redirect, request, url_for

from app.access import bp
from app.models.account import authenticate_user, create_account, username_exists


@bp.route("/")
def index():
    return render_template("access/index.html")


@bp.route("/signin", methods=["POST", "GET"])
def signin_page():
    id = session.get("id")
    if id is not None:
        return redirect(url_for("finance.dashboard_page"))
    
    if request.method == "POST":
        if "signup_button" in request.form:
            return redirect(url_for("access.signup_page"))
        
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        
        result = authenticate_user(username, password)
        # If authentication fails...
        if result < 0:
            if result == -1:
                return render_template("access/signin.html", error_message="Account doesn't exist")
            elif result == -2:
                return render_template("access/signin.html", error_message="Incorrect password")

        # Store user data in session
        session["id"] = result
        session["username"] = username
        return redirect(url_for("finance.dashboard_page"))
    else:
        return render_template("access/signin.html", error_message="‏‏‎ ‎")


@bp.route("/signup", methods=["POST", "GET"])
def signup_page():
    id = session.get("id")
    if id is not None:
        return redirect(url_for("finance.dashboard_page"))
    
    if request.method == "POST":
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        repassword = request.form["RePassword"]
        initial_balance = request.form["initial_balance"]
        
        # Error checks
        if username.isspace() or username == "" or password.isspace() or password == "":
            return render_template("access/signup.html", error_message="Username or password cannot be empty or only spaces")
        
        if username_exists(username):
            return render_template("access/signup.html", error_message="Account with username already exists")
        
        if password != repassword:
            return render_template("access/signup.html",error_message="Passwords do not match")
        
        if not create_account(username, password, initial_balance):
            return render_template("access/signup.html", error_message="Failed to create account")
        else:
            return redirect(url_for("access.signin_page"))
    else:
        # Blank characters to keep formatting of page correct.
        return render_template("access/signup.html", error_message="‏‏‎ ‎")
    
@bp.route("/signout", methods=["POST", "GET"])
def signout():
    # Remove user specific data
    session.pop("id")
    session.pop("username")
    
    # Redirect to sigin page
    return redirect(url_for("access.signin_page"))

