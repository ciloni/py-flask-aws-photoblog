from flask import Flask

from src.routes.AppRoutes import AppRoutes
from src.routes.UsersRoutes import UsersRoutes

def create_app():
    app = Flask(__name__,template_folder="views/")

    app.register_blueprint(AppRoutes, url_prefix='/')

    app.register_blueprint(UsersRoutes, url_prefix='/users/')

    return app