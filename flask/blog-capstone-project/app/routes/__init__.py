from app.routes.web.blog import blog_bp
from app.routes.api.blog_api import blog_api_bp

def register_routes(app):
    app.register_blueprint(blog_bp)
    
    app.register_blueprint(blog_api_bp, url_prefix='/api')