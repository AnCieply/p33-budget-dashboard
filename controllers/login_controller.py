from flask import render_template, request, url_for

from init import app
from models.login_model import authenticate_user

@app.route("/login", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        
        result = authenticate_user(username, password)
        # If authentication fails...
        if result < 0:
            if result == -1:
                return "Account doesn't exist"
            elif result == -2:
                return "Wrong Password"

        return str(result)
    else:
        return render_template("login.html")
