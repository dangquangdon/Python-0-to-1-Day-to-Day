import os
import secrets
from flask import current_app, url_for
from PIL import Image
from app import mail
from flask_mail import Message


def save_picture(pic):

    random_hex = secrets.token_hex(8)

    _, file_ext = os.path.splitext(pic.filename)

    picture_filename = random_hex + file_ext

    picture_path = os.path.join(current_app.root_path,
                                'static/img/profile_pics',
                                picture_filename)
    output_size = (250,250)
    img = Image.open(pic)
    img.thumbnail(output_size)

    img.save(picture_path)

    return picture_filename

def send_reset_email(user):
    token = user.get_reset_token()
    # First argument is Subject
    msg = Message('Password Reset Request',
                  sender='noreply@python0to1.com',
                  recipients=[user.email])
    msg.body = f""" To reset your password, click to the link below:
    {url_for('auth.reset_token', token=token, _external=True)}

    If it was not you who made this request, please ignore this email.
    """
    # _external=True means that return the url in full url, with the domain name.

    mail.send(msg)
