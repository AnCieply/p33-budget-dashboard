# p33-budget-dashboard
A budget management application created for the P33 project.

## Tech Stack
### Frontend
HTML and CSS

### Backend
Python\
Flask\
Azure SQL

## Setup
### Windows **MAY NOT WORK**
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

Install dependencies
```
pip install flask flask_sqlalchemy bcrypt
```
Finally, to run the app, run the following command in the project's root
```
python app.py
```


### Ubuntu **RECOMMENDED ON WSL**
Install python and dependencies
```
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip python3-virtualenv build-essential libffi-dev
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
Install dependencies
```
pip install flask flask_sqlalchemy bcrypt
```
Finally, to run the app, run the following command in the project's root
```
python3 app.py
```
