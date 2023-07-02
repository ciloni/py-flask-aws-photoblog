from flask import Blueprint

from src.controllers.AppController import index, login, logout, profile

AppRoutes = Blueprint('app_routes',__name__)

AppRoutes.route('/', methods=['GET'])(index)
AppRoutes.route('/login',methods=['GET','POST'])(login)
AppRoutes.route('/logout',methods=['GET'])(logout)
AppRoutes.route('/<useraccount>',methods=['GET'])(profile)