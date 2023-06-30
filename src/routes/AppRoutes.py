from flask import Blueprint

from src.controllers.AppController import index, login

AppRoutes = Blueprint('app_routes',__name__)

AppRoutes.route('/', methods=['GET'])(index)
AppRoutes.route('/login',methods=['GET','POST'])(login)