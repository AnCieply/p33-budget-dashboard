from init import app
from models.account_creation_model import create_account
from flask import redirect, request, render_template

@app.route("/accountcreation", methods=["POST", "GET"])
def acccount_creation_page():
    if request.method == "POST":
        # User input from view
        username = request.form["Username"]
        password = request.form["Password"]
        
        if not create_account(username, password):
            return "Failed to create account"
        else:
            return redirect("/login")
    else:
        return render_template("createaccount.html")
