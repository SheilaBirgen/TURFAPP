from app import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 
from werkzeug.security import generate_password_hash,check_password_hash

# class User(db.Model,UserMixin):

# class Turfs(db.model):    