import os
from flask import Flask
from .config import config_by_name
from .extensions import db, migrate
from .main import main_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)

    return app
