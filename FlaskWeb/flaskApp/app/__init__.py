from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_type):
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(),"config",config_type+".py")
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register routes
    from app.auth import auth
    from app.posts import posts

    app.register_blueprint(auth)
    app.register_blueprint(posts)

    return app
