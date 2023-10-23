from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import urandom

# App and database initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.secret_key = urandom(24)
db = SQLAlchemy(app)
