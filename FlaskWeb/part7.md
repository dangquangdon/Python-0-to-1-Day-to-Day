# User Account Page

This page is for user to update information and profile picture

1. First, let's style the account page quickly with bootstrap 4

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container p-5">
    <div class="row">
      <div class="col-sm-6 text-center">
        <img src="static/img/profile_pics/{{current_user.image_file}}" alt="avatar" class="ava">
      </div>
      <div class="col-sm-6 text-center">
        <h1>{{current_user.username}}</h1>
        <p class="lead">{{current_user.email}}</p>
      </div>
    </div>
  </div>
{% endblock content %}
```

2. We will need to store profile picture in `static/img/profile_pics` so let's create these folders.

And as we set in `User` model that user will have a default profile picture, so we will also need to put to `profile_pics` folder a picture, and name it `default.jpg`

3. In order to let users update username, email address and profile picture, we will need a form to do so.

So we will create a new form class in `auth/forms.py`, and this new class is very similar to `RegistrationForm` class, except that we don't need the `password` and `confirm_password` fields.

Also, the validations methods that we use to check if the username and email have been used need to modify. Because, if the user doesn't want to change both but either, or just profile pictures, then when he/she hit the Update button, it will throw and error and said that this username and password have been used, which is True.

So what we want to do is to only do these validation checks if the current username and email are different

```python
from flask_login import current_user

class UpdateAccount(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(),
                           Length(min=2, max=20)
                           ])
    email = StringField("Email", validators=[
                            DataRequired(),
                            Email()
                        ])

    submit = SubmitField('Update')


        # Validated usernames and emails
    def validate_username(self, username):
      if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()

        if user:
          raise ValidationError('The username has been taken. Please choose another one!')

    def validate_email(self, email):
      if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()

        if user:
          raise ValidationError("This email was used, please login or reset password if you've forgoten")
```

4. Back to the `auth/routes.py`

```python
from app.auth.forms import UpdateAccount

...
def account():
  form = UpdateAccount()
  return render_template('account.html', form=form)
```

5. Now we have to insert the form fields to the `html` files the same way that we did for `register` and `login` page.

Since this is the form to update user's info, we should display the current user's info in the form. In the `account` route

```python
@auth.route('/account', methods = ['GET','POST'])
@login_required
def account():
  form = UpdateAccount()
  if form.validate_on_submit():
    curren_user.username = form.username.data
    current_user.email = form.eamil.data
    db.session.commit()
    flash("Account has been updated!" , 'success')
    return redirect(url_for('auth.account'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.email.data = current_user.email
    ...
```

6. As mentioned, We want user to be able to update and change profile picture, therefore we need to add a new form field to upload file. So back to the `auth/forms.py`

```python
from flask_wtf.file import FiledField, FileAllowed

class UpdateAccount(FlaskForm):
  ...
  picture = FileField('Update Profile Picture',
                      validators=[FileAllowed(['jpg','png','jpeg','gif'])])
  ...
```

In the `account.html`, add new form field to the page

```html
  <div class="form-group">
    {{ form.picture.label(class="form-control-label") }}
    {{ form.picture(class="form-control-file") }}
    {% if form.picture.errors %}
      {% for err in form.picture.errors %}
        <span class="text-danger">{{err}}</span>
      {% endfor %}
    {% endif %}
  </div>
```

Note that, in the `<form>` tag, we have to add the `enctype="multipart/form-data"` attribute in order to make the file upload work properly.

7. In order to be able to save the uploaded picture, we will create a separate helper function out of the `account` route to keep the code inside the `route` clean. In `auth` create new file `utils.py`

```python
import secrets # remember this ? ^^!
import os
from flask import url_for, current_app


def save_picture(pic):
  # Generate a random name for the picture
  random_hex = secrets.token_hex(8)
  # To keep the extension of the file stay the same
  # the _ is actual file_name, but we don't use it so we turn it into _ to indicate unused variable
  _, file_ext = os.path.splitext(pic.filename)
  picture_filename = random_hex + file_ext
  picture_path = os.path.join(current_app.root_path,
                              'static/img/profile_pics',
                              picture_filename)
  pic.save(picture_path)

  # we only need to return the file name of the picture
  return picture_filename

```
In `auth/routes.py`

```python
from app.auth.utils import save_picture

...
def account():
  ...
  if form.validate_on_submit():
    pic_data = form.picture.data
    if pic_data:
      picture_file = save_picture(pic_data)
      current_user.image_file = picture_file
  ...
```

8. Now that we are able to upload the picture properly, however, we have to also resize the pictures that users upload to keep the file small enough, won't take so much of our memory size as well as keep the page loads faster.

We need to install `Pillow` to do so

`pip install Pillow`

Back to `utils.py`

```python
from PIL import Image

def save_picture(pic):

  ...
  output_size = (250,250)

  img = Image.open(pic)
  img.thumbnail(output_size)

  img.save(picture_path)

  return picture_filename
