# p33-budget-dashboard
A budget management application created for the P33 project.

## Tech Stack
### Frontend
HTML and CSS

### Backend
Python\
Flask\
PostgreSQL

## Dev Setup
### Ubuntu
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
pip install -r requirements.txt
```
Set flask-related environment variables
```
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
```
Finally, to run the app, run the following command in the project's root
```
flask run
```
