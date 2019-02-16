from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(),
                           Length(min=2, max=20)
                           ])
    email = StringField("Email", validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField("Password", validators=[
                             DataRequired()
                             ])
    confirm_password = PasswordField("Confirm Password", validators=[
                                     DataRequired(),
                                     EqualTo('password')])
    submit = SubmitField('Sign Up')


        # Validated usernames and emails
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
          raise ValidationError('The username has been taken. Please choose another one!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
          raise ValidationError("This email was used, please login or reset password if you've forgoten")



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField("Password", validators=[
                             DataRequired()
                             ])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')


class UpdateAccount(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(),
                           Length(min=2, max=20)
                           ])
    email = StringField("Email", validators=[
                            DataRequired(),
                            Email()
                        ])
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])

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
