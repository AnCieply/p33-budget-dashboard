from init import app

from controllers import index_controller
from controllers import login_controller
from controllers import account_creation_controller
from controllers import dashboard_controller

if __name__ == "__main__":
    app.run(debug=True)
    