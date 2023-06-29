from flask import Blueprint

from src.controllers.AppController import index

AppRoutes = Blueprint('app_routes',__name__)

AppRoutes.route('/', methods=['GET'])(index)
