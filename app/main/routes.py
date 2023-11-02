from flask import render_template, url_for

from app.main import bp
from app.extensions import db


@bp.route("/")
def index():
    db.create_all()
    return redirect(url_for("access.signin"))

