from flask import Blueprint

from src.controllers.PostsController import create, update, read, delete

PostsRoutes = Blueprint('posts_routes',__name__)

PostsRoutes.route('create/', methods=['GET','POST'])(create)
