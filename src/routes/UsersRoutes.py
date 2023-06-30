from flask import Blueprint

from src.controllers.UsersController import create, update, read, delete

UsersRoutes = Blueprint('users_routes',__name__)

UsersRoutes.route('create/', methods=['GET','POST'])(create)
