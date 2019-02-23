from app import db
from datetime import datetime
from app.posts.models import Post
from app import login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),
                           nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expire_sec=1800): # 30mins
        s = Serializer(current_app.config['SECRET_KEY'], expire_sec)
        token = s.dumps({'user_id': self.id}).decode('utf-8')
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
          user_id = s.loads(token)['user_id']
        except:
          return None
        print(user_id)
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
