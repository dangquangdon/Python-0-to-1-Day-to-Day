# Part 6: User Authentication

1. Before we start with taking users' credentials and store them in database, we have to implement the password hashing first, to secure the users' passwords. We are going to use `flask-bcrypt`
Run `pip install flask-bcrypt`

2. Run `python` in terminal/command prompt to test it out
```python
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('test password')
# Python will generate a hashed password, and it will be bytes (python 3 new datatype )
# to convert it into string
>>> bcrypt.generate_password_hash('test password').decode('utf-8')
# Each time we run this again, it will generate a new hashed string, event though the original password is still the same
# To check if the password after hashed is equal to the original password
>>> hashed_password = bcrypt.generate_password_hash('test password').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_password, 'test password') # return True
```

3. In the `__init__.py` of the app and start to import `flask_bcrypt`
```python
from flask_bcrypt import Bcrypt
...
# Create a new instance of Bcrypt
bcrypt = Bcrypt()
# in create_app()
def create_app(config_type):
  ...
  bcrypt.init_app(app)
```

4. Setup the logic for the registration route:
- Firstly, after we receive the password that users have input in the form, we have to hash it before storing it to database. So in the `auth.routes`, import `bcrypt` and `db`, and in `if form.validate_on_submit()`
```python
hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
new_user = User(username = form.username.data,
                email = form.email.data,
                password = hashed_password)
db.session.add(user)
db.session.commit()
...
return redirect(url_for(auth.login))
```

5. Now we can let an user to register and the data is stored in database. However, we have to implement a check to make sure this user has already registered or not, or else SQLAlchemy will throw errors. One way of doing this is to write a check in the register route. However, we are going to do it in a different way.
They way we are going to do is to add a custom validation to the `RegistrationForm`
```python
from app.models  import User
from wtforms.validators import  ValidationError

class RegistrationForm(FlaskForm):
  ....
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()

    if user:
      raise ValidationError('The username has been taken. Please choose another one!')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()

    if user:
      raise ValidationError('This email has been used! Please login or reset password')
```

6. Now that we can handle the user registration, next we will work on handling user log in and out. To do this, we will use another extension call `Flask-Login`

`pip install flask-login`

In the `__init__.py` of `app`

```python
from flask_login import LoginManager

...

login_manager = LoginManager()

def create_app(config_type):
  ...

  login_manager.init_app(app)

```

Back to the `models.py` of `auth`

```python
from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  ...
```

- The function that we've defined above, together with the decorator will keep the users logged in event if they refresh the page

- The `login_manager` would expect our models to have some certain attributes:
  - `is_authenticated`: return `True` if users provide valid credentials
  - others: `is_active`, `is_annonymous`, `get_id`

- We could add these ourselves, but `flask_login` provides us already with `UserMixin` class that has all of those attributes.

- So we set our `User` class to inherit also from `UserMixin`

7. Now in the `routes.py` of `auth`, we can replace the dummies data with the actual login check in `def login()` route

```python
from flask_login import login_user

...

if form.validate_on_submit():
  user = User.query.filter_by(email=form.email.data).first()
  input_password = form.password.data
  if user and bcrypt.check_password_hash(user.password, input_password):
    login_user(user, remember = form.remember.data)
    return redirect(url_for('posts.home'))
  ...
```

8. Now that the users can login, we have to handle their sessions so that they cannot go to login page or register page again because they don't need them anymore.

In the `routes.py` of `auth`

```python
from flask_login import login_user, current_user

...

def register():
  if current_user.is_authenticated:
    redirect(url_for('posts.home'))



...


def login():
  if current_user.is_authenticated:
    redirect(url_for('posts.home'))

```

