from flask import render_template, session, request, make_response, url_for, redirect

from init import app
from models.login_model import authenticate_user

@app.route("/login", methods=["POST", "GET"])
def login_page():
    id = session.get("id")
    if id is not None:
        return redirect("/dashboard")
    
    if request.method == "POST":
        if "signup_button" in request.form:
            return redirect("/signup")
        
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        
        result = authenticate_user(username, password)
        # If authentication fails...
        if result < 0:
            if result == -1:
                return render_template("login.html", error_message="Account doesn't exist")
            elif result == -2:
                return render_template("login.html", error_message="Incorrect password")

        # Store user data in session
        session["id"] = result
        session["username"] = username
        return redirect("/dashboard")
    else:
        return render_template("login.html", error_message="‏‏‎ ‎")
