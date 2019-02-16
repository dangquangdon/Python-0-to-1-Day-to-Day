import os
import secrets
from flask import current_app
from PIL import Image


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
