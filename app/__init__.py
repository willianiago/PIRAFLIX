from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    from .movies import movies as movies_blueprint
    app.register_blueprint(movies_blueprint, url_prefix='/movies')


    from .import routes
    routes.init_app(app)
    return app

