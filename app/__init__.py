import os

from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret string")


login_manager = LoginManager()
login_manager.init_app(app)


