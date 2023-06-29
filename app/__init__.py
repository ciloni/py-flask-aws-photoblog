from flask import Flask

from src.routes.AppRoutes import AppRoutes

def create_app():
    app = Flask(__name__,template_folder="views/")

    app.register_blueprint(AppRoutes, url_prefix='/')

    return app