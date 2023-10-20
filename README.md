# p33-budget-dashboard
A budget management application created for the P33 project

## Tech Stack
### Frontend
HTML and CSS

### Backend
Python\
Flask\
SQLite3

## Setup
### Windows
Install python

Clone the git repo and open in powershell

Install virtualenv
```
pip install virtualenv
```
Run the following command to create the python virtual environment
```
python -m virtualenv env
```
Activate the environment
```
.\env\Scripts\activate.ps1
```
If you get any issues with running this script, run this command first:
```
Set-ExecutionPolicy -Scope CurrentUser unrestricted
```

Install flask and flask_sqlalchemy
```
pip install flask flask_sqlalchemy
```
Finally, to run the app, run the following command in the project's root
```
python app.py
```


### Ubuntu
Install python and dependencies
```
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip python3-virtualenv
```
Clone the git repo and open in terminal

Run the following command to create the python virtual environment
```
virtualenv env
```
Activate the environment
```
source env/bin/activate
```
Install flask and flask_sqlalchemy
```
pip install flask flask_sqlalchemy
```
Finally, to run the app, run the following command in the project's root
```
python3 app.py
```

## Screenshots
![Login Page](/screenshots/login.png?raw=true "Login Page")
![Signup Page](/screenshots/signup.png?raw=true "Signup Page")
![Dashboard Page](/screenshots/dashboard.png?raw=true "Dashboard Page")
![Report Page](/screenshots/report.png?raw=true "Report Page")
![Spending Plan Page](/screenshots/spendingplan.png?raw=true "Spending Plan Page")
