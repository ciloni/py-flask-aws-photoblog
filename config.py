import os



class Config():
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photoblog.db'
    UPLOAD_FOLDER = '/static/temp'
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024

