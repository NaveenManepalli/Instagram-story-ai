from flask import Flask
from flask_jwt_extended import JWTManager

from config import Config
from database.db import db

from auth_service.routes import auth_bp
from app_service.story.routes import story_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(story_bp, url_prefix="/story")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)