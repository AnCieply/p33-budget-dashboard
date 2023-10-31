from init import app
from models.signup_model import create_account, username_exists
from flask import redirect, session, request, render_template

@app.route("/signup", methods=["POST", "GET"])
def signup_page():
    id = session.get("id")
    if id is not None:
        return redirect("/dashboard")
    
    if request.method == "POST":
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        repassword = request.form["RePassword"]
        initial_balance = request.form["initial_balance"]
        
        # Error checks
        if username.isspace() or username == "" or password.isspace() or password == "":
            return render_template("signup.html", error_message="Username or password cannot be empty or only spaces")
        
        if username_exists(username):
            return render_template("signup.html", error_message="Account with username already exists")
        
        if password != repassword:
            return render_template("signup.html",error_message="Passwords do not match")
        
        if not create_account(username, password, initial_balance):
            return render_template("signup.html", error_message="Failed to create account")
        else:
            return redirect("/login")
    else:
        # Blank characters to keep formatting of page correct.
        return render_template("signup.html", error_message="‏‏‎ ‎")
