from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, default=0)
    username = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=0.0)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        username = request.form["Username"]
        password = request.form["Password"]

        try:
            account = db.session.query(Account).filter(Account.username==username).one()
            if account.password != password:
                return "Wrong password"
            return str(account.id)
        except:
            return "Failed to login"
    else:
        return render_template("login.html")
    
@app.route("/createaccount", methods=["POST", "GET"])
def create_account_page():
    if request.method == "POST":
        username = request.form["Username"]
        password = request.form["Password"]
        
        try:
            new_account = Account()
            new_account.username = username
            new_account.password = password
            new_account.id = db.session.query(Account).count() + 1
            
            db.session.add(new_account)
            db.session.commit()
            
            return redirect("/login")
        except:
            return "Failed to create account"
    else:
        return render_template("createaccount.html")

if __name__ == "__main__":
    app.run(debug=True)
    