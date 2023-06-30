from flask import Flask
from config import Config
from flask_login import LoginManager


from src.routes.AppRoutes import AppRoutes
from src.routes.UsersRoutes import UsersRoutes

from database import db

from src.models.UsersModel import User

def create_app(config_class=Config):
    app = Flask(__name__,template_folder="views/")
    app.config.from_object(config_class)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'app_routes.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.one_or_404(db.select(User).filter_by(id=user_id))

    app.register_blueprint(AppRoutes, url_prefix='/')

    app.register_blueprint(UsersRoutes, url_prefix='/users/')

    return app