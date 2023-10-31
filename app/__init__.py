from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from app.extensions import db


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions
    db.init_app(app)
    
    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.access import bp as access_bp
    app.register_blueprint(access_bp, url_prefix="/access")
    
    from app.finance import bp as finance_bp
    app.register_blueprint(finance_bp, url_prefix="/finance")
    
    return app

