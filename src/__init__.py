from flask import Flask
from .home import home_bp
from .tables import table_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(table_bp)
    return app
