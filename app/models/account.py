from sqlalchemy import select
from bcrypt import hashpw, gensalt
from json import dumps

from app.extensions import db
import traceback

class Account(db.Model):
    id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False, primary_key=True)
    password = db.Column(db.LargeBinary, nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)


def authenticate_user(username: str, password: str) -> int:
    try:
        # Get account data
        account = db.session.execute(select(Account).filter_by(username=username)).scalar_one()
        # Hash inputted password
        password = password.encode("utf-8")
        hash_pw = hashpw(password, account.salt)
        
        if account.password != hash_pw:
            return -2 # Wrong password
        return account.id
    except:
        print(traceback.format_exc())
        return -1 # Doesn't exist


def username_exists(username: str):
    try:
        # If an account with username doesn't exist, exception is thrown
        db.session.execute(select(Account).filter_by(username=username)).scalar_one()
        return True
    except:
        return False

    
def create_account(username: str, password: str, initial_balance: float):
    try:
        if username_exists(username):
            return False
        
        # Hash password and generate salt
        password = password.encode("utf-8")
        salt = gensalt()
        hash_pw = hashpw(password, salt)
        
        new_account = Account()
        new_account.username = username
        new_account.password = hash_pw
        new_account.salt = salt
        new_account.id = db.session.query(Account).count() + 1
        
        from app.models.user_data import UserData
        new_data = UserData()
        new_data.id = new_account.id
        new_data.balance = initial_balance
        new_data.transactions = dumps([])
        
        db.session.add(new_account)
        db.session.add(new_data)
        db.session.commit()
        return True
    except:
        print(traceback.format_exc())
        return False

