from init import db
from models.db_models import Account, UserData
import bcrypt

def username_exists(username: str):
    try:
        # If an account with username doesn't exist, exception is thrown
        db.session.query(Account).filter(Account.username == username).one()
        return True
    except:
        return False
    
def create_account(username: str, password: str):
    try:
        if username_exists(username):
            return False
        
        # Hash password and generate salt
        password = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hash_pw = bcrypt.hashpw(password, salt)
        
        new_account = Account()
        new_account.username = username
        new_account.password = hash_pw
        new_account.salt = salt
        new_account.id = db.session.query(Account).count() + 1
        
        new_data = UserData()
        new_data.id = new_account.id
        new_data.balance = 0.0
        
        db.session.add(new_account)
        db.session.add(new_data)
        db.session.commit()
        return True
    except:
        return False
