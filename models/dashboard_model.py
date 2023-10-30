from init import db
from models.db_models import UserData

import json
from sqlalchemy import select

def register_transaction(user_id: int, acc: str, date: str, category: str, amount: float, pos: bool):
    # Create dict representing transaction
    transaction = {
            "Account": acc,
            "Date": date,
            "Category": category,
            "Amount": float(amount),
            "Pos": pos
    }
    
    # Get user data object from database
    user_data = db.session.execute(select(UserData).filter_by(id=user_id)).scalar_one()
    
    # Deserialize transaction list and append transaction
    user_trans: list = json.loads(user_data.transactions)
    user_trans.append(transaction)
    
    # Update user data object and commit changes
    user_data.transactions = json.dumps(user_trans)
    db.session.commit()


def get_user_balance(id: int):
    try:
        user_data = db.session.query(UserData).filter(UserData.id == id).one()
        return user_data.balance
    except:
        return -0.0
