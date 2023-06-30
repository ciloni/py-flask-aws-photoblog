from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from src.models import UsersModel
from src.models import PostsModel