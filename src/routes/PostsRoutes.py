from flask import Blueprint

from src.controllers.PostsController import create, update, read, delete

PostsRoutes = Blueprint('posts_routes',__name__)

PostsRoutes.route('create/', methods=['GET','POST'])(create)
PostsRoutes.route('read/<useraccount>/<postid>', methods=['GET'])(read)
PostsRoutes.route('update/<useraccount>/<postid>', methods=['GET','POST'])(update)
PostsRoutes.route('delete/<useraccount>/<postid>', methods=['GET'])(delete)
