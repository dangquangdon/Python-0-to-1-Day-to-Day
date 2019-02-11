from flask import Blueprint

posts = Blueprint('posts', __name__)

from app.posts import routes
