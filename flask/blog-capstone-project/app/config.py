import os

class Config:
    SECRET_KEY = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"  
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'post.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
