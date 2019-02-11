from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app(config_type):
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(),"config",config_type+".py")
    app.config.from_pyfile(configuration)

    db.init_app(app)


    # Register routes
    from app.auth import auth
    from app.posts import posts

    app.register_blueprint(auth)
    app.register_blueprint(posts)

    return app
