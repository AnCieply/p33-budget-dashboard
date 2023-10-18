from init import db
from models.db_models import Account

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
        
        new_account = Account()
        new_account.username = username
        new_account.password = password
        new_account.id = db.session.query(Account).count() + 1
        
        db.session.add(new_account)
        db.session.commit()
        return True
    except:
        return False
