import os
from flask import Flask
from app.models.user import Users
from app.routes import register_routes
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

from app.config import Config  
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    CKEditor(app)
    Bootstrap(app)
    os.makedirs(os.path.join(Config.basedir, 'instance'), exist_ok=True)
    
    register_routes(app)

    db.init_app(app)
    login_manager.init_app(app) 
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    
    with app.app_context():
        try:
            from app.models import post, user, comment
            db.create_all()  
            print("Database and tables created successfully!")
        except Exception as e:
            print(f"Error: {e}")
    
    return app


