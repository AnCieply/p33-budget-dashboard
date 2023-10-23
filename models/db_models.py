from init import db

class Account(db.Model):
    id = db.Column(db.Integer, default=0)
    username = db.Column(db.String(100), nullable=False, primary_key=True)
    password = db.Column(db.LargeBinary, nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0.0)
