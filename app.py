from init import app

from controllers import index_controller
from controllers import login_controller
from controllers import signup_controller
from controllers import dashboard_controller
from controllers import report_controller
from controllers import spending_plan_controller

if __name__ == "__main__":
    app.run(debug=True)
    