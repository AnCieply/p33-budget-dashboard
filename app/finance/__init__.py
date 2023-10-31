from flask import Blueprint


bp = Blueprint("finance", __name__)


# Registers a blueprint's routes as the blueprint is registered
from app.finance import routes

