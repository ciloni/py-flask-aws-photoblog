from flask import Flask
from config import Config


from src.routes.AppRoutes import AppRoutes
from src.routes.UsersRoutes import UsersRoutes

from database import db

def create_app(config_class=Config):
    app = Flask(__name__,template_folder="views/")
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(AppRoutes, url_prefix='/')

    app.register_blueprint(UsersRoutes, url_prefix='/users/')

    return app