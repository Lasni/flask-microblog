from flask import Blueprint

bp = Blueprint("api", __name__)

# import after the blueprint is created to avoid circular imports
from app.api import users, errors, tokens