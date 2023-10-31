from flask import Blueprint


bp = Blueprint("main", __name__)


# Registers a blueprint's routes as the blueprint is registered
from app.main import routes

