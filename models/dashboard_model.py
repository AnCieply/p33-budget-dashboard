from init import db
from models.db_models import UserData

def get_user_balance(id: int):
    try:
        user_data = db.session.query(UserData).filter(UserData.id == id).one()
        return user_data.balance
    except:
        return -0.0
