import os

from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv

from .blueprints.authentication import authentication
from .database.repository import UserRepository


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret string")

app.register_blueprint(authentication)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: int):
    return UserRepository.get_user(user_id)
