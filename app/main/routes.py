from flask import render_template

from app.main import bp
from app.extensions import db
from app.models.user_data import create_budget_category


@bp.route("/")
def index():
    db.create_all()
    return render_template("index.html")

