from init import db
from models.db_models import Account

def authenticate_user(username: str, password: str):
    try:
        # Get account data
        account = db.session.query(Account).filter(Account.username == username).one()
        if account.password != password:
            return -2 # Wrong password
        return account.id
    except:
        return -1 # Doesn't exist
    