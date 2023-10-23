from flask import redirect
from init import app, db

# Index Controller
@app.route("/")
def index():
    db.create_all()
    return redirect("/login")
