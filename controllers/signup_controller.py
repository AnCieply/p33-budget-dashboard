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
        
        if username.isspace() or username == "" or password.isspace() or password == "":
            return render_template("signup.html", space_or_empty="True")
        
        if username_exists(username):
            return "Account with username already exists"
        
        if not create_account(username, password):
            return "Failed to create account"
        else:
            return redirect("/login")
    else:
        return render_template("signup.html")
