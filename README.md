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
#### Windows steps coming later
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
Finally, to run the app, run the following command in the projects root
```
python3 app.py
```
