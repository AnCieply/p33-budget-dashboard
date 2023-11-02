from flask import url_for, redirect

from app.main import bp
from app.extensions import db


@bp.route("/")
def index():
    db.create_all()
    return redirect(url_for("access.signin"))

