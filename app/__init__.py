from flask import Flask
from .routes import pokenea_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pokenea_bp)
    return app