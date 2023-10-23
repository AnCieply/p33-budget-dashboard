from init import db
from models.db_models import Account
import bcrypt

def authenticate_user(username: str, password: str):
    try:
        # Get account data
        account = db.session.query(Account).filter(Account.username == username).one()
        # Hash inputed password
        password = password.encode("utf-8")
        hash_pw = bcrypt.hashpw(password, account.salt)
        
        if account.password != hash_pw:
            return -2 # Wrong password
        return account.id
    except:
        return -1 # Doesn't exist
    