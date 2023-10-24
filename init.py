from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib
from os import urandom

# App and database initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql://p33shadowadmin:LongWill2@p33.database.windows.net:1433/P33Data?driver=ODBC+Driver+18+for+SQL+Server"
app.secret_key = urandom(24)

db = SQLAlchemy(app)
