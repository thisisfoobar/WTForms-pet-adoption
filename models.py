"""Models for pet adoption app"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets table"""

    __tablename__ = "pets"

    default_photo = "https://www.publicdomainpictures.net/pictures/500000/nahled/cute-cat-cartoon-clipart-1676633710TRA.jpg"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text,
                          default=default_photo,
                          nullable=True)
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=1)
    
