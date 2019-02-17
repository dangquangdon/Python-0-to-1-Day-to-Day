from flask import Blueprint

err = Blueprint('err', __name__)

from app.error import routes
