from sqlalchemy import select, Result
from json import loads, dumps
import traceback

from app.extensions import db


class UserData(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    transactions = db.Column(db.JSON, nullable=False)


def get_user_data(user_id: int) -> UserData:
    try:
        user_data = db.session.execute(select(UserData).filter_by(id=user_id)).scalar_one()
        return user_data
    except:
        print("Failed to get data of user id " + user_id)


def get_user_balance(user_id: int) -> float:
    try:
        user_data = get_user_data(user_id)
        return user_data.balance
    except:
        return -0.0


def modify_user_balance(user_id: int, balance_change: float):
    try:
        user_data = get_user_data(user_id)
        user_data.balance = user_data.balance + balance_change
        db.session.commit()
    except:
        print("Failed to modify balance of user id " + user_id)


def add_user_transaction(user_id: int, account: str, date: str, category: str, amount: float, pos: bool):
    try:
        # Create dict representing transaction
        transaction = {
                "Account": account,
                "Date": date,
                "Category": category,
                "Amount": float(amount),
                "Pos": pos
        }

        # Get user transaction data from database 
        user_data = get_user_data(user_id)
        transactions_json = user_data.transactions

        # Deserialize transaction list and append transaction
        transactions_list: list = loads(transactions_json)
        transactions_list.append(transaction)

        # Update user data object and commit changes
        transactions_json = dumps(transactions_list)
        user_data.transactions = transactions_json
        db.session.commit()
    except:
        print(traceback.format_exc())