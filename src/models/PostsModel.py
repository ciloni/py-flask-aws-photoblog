from database import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer) # Foreign Key
    post_description = db.Column(db.String(1000))
    post_mediatype = db.Column(db.String(4))
    post_mediapath = db.Column(db.String(255))
    post_filename = db.Column(db.String(30))
    post_datecreated = db.Column(db.DateTime())

    def __repr__(self):
        return f'<Id "{self.id}">'
    
    def __init__(self, user_id, post_description, post_mediatype, post_mediapath, post_filename):
        self.user_id = user_id
        self.post_description = post_description
        self.post_mediatype = post_mediatype
        self.post_mediapath = post_mediapath
        self.post_filename = post_filename
        self.post_datecreated = datetime.now()
