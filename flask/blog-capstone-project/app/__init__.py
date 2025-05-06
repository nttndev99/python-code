import os
from flask import Flask
from app.routes import register_routes
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor

from app.config import Config  
from app.extensions import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    CKEditor(app)
    Bootstrap(app)
    register_routes(app)
    
    os.makedirs(os.path.join(Config.basedir, 'instance'), exist_ok=True)
    db.init_app(app)
    

    with app.app_context():
        try:
            from app.models import post
            db.create_all()  
            print("Database and tables created successfully!")
        except Exception as e:
            print(f"Error: {e}")
        
    return app


