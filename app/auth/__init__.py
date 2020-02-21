from flask import Blueprint
name = Blueprint('auth', __name__)
from . import forms,views