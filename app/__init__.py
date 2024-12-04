from flask import Flask
import config


def create_app():
    app = Flask(__name__)

    from .import routes
    routes.init_app(app)
    return app