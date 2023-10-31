from flask import Blueprint


bp = Blueprint("access", __name__)


# Registers a blueprint's routes as the blueprint is registered
from app.access import routes

