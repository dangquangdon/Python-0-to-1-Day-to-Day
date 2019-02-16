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
    return redirect(url_for('posts.home'))



...


def login():
  if current_user.is_authenticated:
    return redirect(url_for('posts.home'))

```

9. Next step is to make a logout route to let user logout. So in our `app.auth.route`

```python
from flask_login import logout_user

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('posts.home'))
```
`logout_user` function from `flask_login` will handle the logging out of the user.

10. Now we have to add the logout button somewhere on the navbar so that user can click to.

Usually, after user has logged in, we don't need to display the `Login` and `Register` buttons anymore, but instead, we will show the `Logout` button. To do so, we will need to put Jinja2's if statement in the `layout.html`

```html
<nav>
...
  <div id="mainNav" class="collapse navbar-collapse">
    <ul class="navbar-nav ml-auto">
    ...

      {% if current_user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" href="/logout">Logout</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/account">Account</a>
        </li>
      {% else %}
      <li class="nav-item">
        <a class="nav-link" href="/login">Login</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/register">Register</a>
      </li>
      {% endif %}
    </ul>

  </div>
</nav>
```

11. We can create for now a `html` file for the `Account` button and a route for it.

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container">
    <h1>Account Page</h1>
    <h2>{{current_user.username}}</h2>
  </div>
{% endblock content %}
```

12. Now if we log in and go to `Account` page, we can see the current user's username. If we logout, we won't see `Account` button anymore, however, if we type `/account` to the end of the url, we can still access the page, but there is no username displayed, because no user has logged in.

What we want to do is to redirect users if they try to access this page without loging in to the login page. In order to do so, we will import a decorator from `flask_login` call `login_required`. In the `app.auth.route`

```python
from flask_login import login_required

@app.route('/account')
@login_required
def account():
  ...
```

To let `flask_login` know that we want it to redirect users to `login` page, we have to set `login_view` in our `app/__init__.py`

```python
...
login_manager = LoginManager()
login_manager.login_view = 'auth.login' #function name of the login route
login_manager.login_message_category = 'warning' # show the category color of the warning message
```

So now, if someone tries to access this protected route `/account` it will redirect him/her to login page with a warning message.

13. For more user friendly, we want to redirect users back to their starting page. Right now, when they log in, they will be redirected to home page, what we are trying to do is that if they try to access protected routes such as `account` route, without logging in, they will be redirected to `login` page, then after they input credentials to log in, we want to redirect them back to `account` page, where they wanted to be at the first place. Let's do that !

- First, after they get redirected to the login page, look at the url, it will have this string `?next=%2Faccount` after the `/login` which indicate that the next page after logging in should be `account`.

- To do so, let's go to the `login` route we will need to import `request` from flask to access the parameter from url

```python
from flask import request

...
def login():
  ...
  login_user(user, remember=form.remember.data)
  next_page = request.args.get('next')
  if next_page:
    return redirect(next_page)
  else:
    return redirect(url_for('posts.home'))
```

14. One last modification in this part. If you've notice, in all of our `<a>` tags, we put the static url links there. Normally it won't be a big problem, however, in case we want to restructure or rename the urls, we have to go to all of the `<a>` tags to change the links. To avoid that, instead of putting static url, we will use the function names that we defined below the `@app.route()`. And we will user `url_for` in Jinja2 syntax. For example

```html
<li class="nav-item">
    <a class="nav-link" href="{{url_for('auth.logout')}}">Logout</a>
</li>
```
