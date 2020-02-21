from flask import Flask
from config import config_options 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])  

    # initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
 
    # configure UploadSetfrom flask import Flask
    # configure_uploads(app,photos)


    return app