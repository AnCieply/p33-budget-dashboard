from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib
from os import urandom

# App and database initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:9132004@localhost:5432/p33"
app.secret_key = urandom(24)

db = SQLAlchemy(app)
