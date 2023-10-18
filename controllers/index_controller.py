from flask import redirect
from init import app

# Index Controller
@app.route("/")
def index():
    return redirect("/login")
