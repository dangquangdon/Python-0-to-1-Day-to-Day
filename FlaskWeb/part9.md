# Part 9: Pagination and Sending Emails


## Pagination

1. So far, we have been able to let users register, login, add post, edit post, and delete post. When we have many posts, it's not a good idea to display all of them in one page. We can just display the top 10 or so. However, we can use Pagination to display all the posts and split them into pages. So let's modify the `home` route

```python
@posts.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=1)

    return render_template("home.html", posts=posts)
```

So instead of using `Post.query.all()` as before, we will use `paginate` function to paginate the posts.
- we will need to grab the page number from the url using `request.args.get('page',1, type=int)`. The second argument is the default page that we want to set, it's `1`. Set the type to `int` to make sure if someone write pagenumber to the url, it must be an `int` or else it will throw and error.

- Then we can pass the page to the paginate function to open the page. `per_page` argument is to indicate how many posts we want to display per page.

- Since we are doing some testing, let's set `per_page` to 1 or 2 only to see the changes

We will also have to adjust `home.html` in order to display the pagination

```html
{% block content %}
  <div class="container">
    {% if posts %}
      {% for post in posts.items %}
      ...
```

Now if we start the server and open `home` page, the posts have been divided into pages. We can try to add `/?page=2` to visite the page number 2 and so on. What we want to do next is to display the button of page numbers, so that users can click to it and jump to next page, not just typing to the url. So in `home.html` after the `for` loop of the posts

```html
<!-- PAGINATION -->
      {% for page in posts.iter_pages() %}
        {% if page %}
          <a href="{{url_for('posts.home', page=page)}}" class="btn btn-outline-primary">{{page}}</a>
        {% else %}
          ...
        {% endif %}
      {% endfor %}
```

If you want to have more customization possibility, please read this [documentation](http://flask-sqlalchemy.pocoo.org/2.3/api/) and test them out.

2. If you notice, our posts is showing the oldest one first and the newest one last. We want to reverse it so that the newest post will always show up in the front page (first page). In the `home` route

```python
posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
```

3. What we will do next, is to set up a route for a specific user's posts. In other word, if we click to a user's name, it should show us all the posts that user has written so far. So in the `auth/routes.py`

```python
@auth.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    # User backslash to break the code into lines
    posts = Post.query.filter_by(author=user)\
                    .order_by(Post.date_posted.desc())\
                    .paginate(page=page, per_page=1)

    return render_template("user_post.html", posts=posts, user=user)
```

Next, we need to create the `user_post.html`, it will be very similar to the `home.html`.

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container">
    <h1>Posts by {{user.username}}</h1>
    <p>Total posts {{posts.total}}</p>
    {% if posts %}
      {% for post in posts.items %}
        <div class="row box p-3 bg-primary my-2 text-white">
          <div class="col-sm-8">
            <h1><a href="{{url_for('posts.single_post', post_id=post.id)}}" class="text-white">
              {{ post.title }}
            </a>
            </h1>
            <h3>{{post.subtitle}}</h3>
            <a href="{{url_for('auth.user_posts', username=post.author.username)}}" class="text-white">
              {{ post.author.username }}
            </a>
            <br>
            <small>{{post.date_posted.strftime('%Y-%m-%d')}}</small>
          </div>
          <div class="col-sm-4">
            <img src="{{ url_for('static', filename='img/profile_pics/'+post.author.image_file) }}">
          </div>
        </div>
      {% endfor %}
      <!-- PAGINATION -->
      {% for page in posts.iter_pages() %}
        {% if page %}
          <a href="{{url_for('auth.user_posts',username=user.username, page=page)}}" class="btn btn-outline-primary">{{page}}</a>
        {% else %}
          ...
        {% endif %}
      {% endfor %}
    {% else %}
      <p>No posts</p>
    {% endif %}
  </div>
{% endblock content %}
```

And now, in the `home` page, we have to change the display of the author's name into a link

```html
{<a href="{{url_for('auth.user_posts', username=post.author.username)}}" class="text-white">
    {{ post.author.username }}
</a>}
```

## Sending emails

4. Let's add a line in the `login` form where usually user can click to it to reset password
```html
<div class="border-top pt-2">
  <small class="text-muted">
  Forget your password? <a href="#">Reset here</a>
  </small>
</div>
```
5. Now we need to have a mechanism to make sure that only someone who has access to the user's email can reset the password, and the reset password link will only valid in the short period of time. First, we will use `itsdangerous` that has been installed along with Flask. Let's see how it works in python interpreter

```python
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer('secret', 30) # Serialize the secret key and set expiration time of 30 seconds
>>> token = s.dumps({'user_id':1}).decode('utf-8') # Tokenize it with the payload contain user's id
>>> s.loads(token) # will return the payload, if more than 30s, it will expire
```

Navigate to the `auth/models.py`

```python
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class User(db.Model, UserMixin):
  ...

  def get_reset_token(self, expires_sec=1800): # 30mins
    s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    token = s.dumps({'user_id': self.id}).decode('utf-8')
    return token

  @staticmethod
  def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None

    return User.query.get(user_id)
```

6. In order to let user reset the password, we will need two new forms, one is to fill in the email to receive reset link, the second one is to fill in new password. So in `auth/forms.py`, let's create those

```python
class RequestForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  submit = SubmitField('Request Password Reset')

  # This validate_email method will check if the email exists.
  # If not it will throw an error message
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError("There is no account. Register first")

class ResetPasswordForm(FlaskForm):
  password = PasswordField("New Password", validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', v
                                   validators=[DataRequired(),
                                              EqualTo('password')])
  submit = SubmitField('Reset')
```

Now, in the `auth/routes.py` let's create new routes

```python
from app.auth.forms import RequestForm, ResetPasswordForm

@auth.route('/reset-password', methods=['GET','POST'])
def reset_password():
  if current_user.is_authenticated:
    return redirect(url_for('posts.home'))

  form = RequestForm()

  return render_template('reset_request.html', form=form)
```

7. Now we create a route for taking new password and reset it

```python
# Right now we have not got the token yet, we will generate it later
@auth.route('/reset-password/<token>', methods=['GET','POST'])
def reset_token(token):
  if current_user.is_authenticated:
    return redirect(url_for('posts.home'))

  user = User.verify_reset_token(token)
  if user is None:
    flash('The request has been expired', 'warning')
    return redirect(url_for('auth.reset_password'))

  form = ResetPasswordForm()
  return render_template('reset_token.html', form=form)
```

Then we will create `reset_token.html` by copying `reset_request.html`

8. Next, we will go to `utils.py` to create a helper function that send email to notify user about the request.

But first, let's install the `flask-mail` extension that help us sending email

`pip install flask-mail`

In order to be able to send email, we will need to do some configuration in our config file. So in `config/dev.py`

```python
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
```

For the admin email credentials, it's best not to expose it in your code, instead, we can set it as environment variables. It's different in MacOS/Linux and Windows.

**In MacOS/Linux**
  ```
  sudo nano ~/.bash_profile
  ```

  When the text editor open, paste/type this
  ```
  export MAIL_USERNAME='your email address'
  export MAIL_PASSWORD='your email password'
  ```
**In Windows 10**

- Go to Search box in Task bar and type `environment variable`
- Click to System Properties/Environment Variable
- In the `User variables` click `New`
- and add `MAIL_USERNAME` and `your email address` to the value box
- do the same for `MAIL_PASSWORD`
Back to `config/dev.py` add `MAIL_USERNAME` and `MAIL_PASSWORD`

```python
import os
...
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

```

9. Go to `app/__init__.py`, let's initialize the `flask_mail` extension

```python
from flask_mail import Mail

mail = Mail()

def create_app():
  ...

  mail.init_app(app)
```

10. Back to `auth/utils.py` let's create a function called `send_reset_email`

```python
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

```

11. Now that we have the two routes set up, let's work on the form validation in each route. Back to `reset_password` route

```python
@auth.route('/reset-password', methods=['GET','POST'])
def reset_password():
  ...

  form = ResetPasswordForm()
      if form.validate_on_submit():
          hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

          user.password = hashed_password
          db.session.commit()
          flash(f"Password has been reset for {user.username} !", 'success')
          return redirect(url_for('auth.login'))

      return render_template('reset_token.html', form=form)
```

## Add custom error page

So we want to customize our error page so it doesn't look boring, let's start a new package in our app call `error`, which will have it own `routes.py` and `__init__.py`.

- In `app` folder, create a new folder called `error`, and inside `error`, create `__init__.py` and `routes.py`. Very similar to other packages' `__init__.py`, we start the blueprint

```python

from flask import Blueprint

err = Blueprint('err', __name__)

from app.error import routes
```

Then we have to register this blueprint to the `__init__.py` of `app` folder

```python
def create_app(config_type):
  ...
  from app.error import err

  ...
  app.register_blueprint(err)

```


However, in the `routes.py` we are going to user different decorator

```python
from app.error import err
from flask import render_template

# There is another method call errorhandler ( not app_errorhandler)
# It is only used to handle errors in the current blueprint, not across packages.

@err.app_errorhandler(404)
def erro_404(err):
    return render_template('err_handle/err_404.html'), 404
    # In flask, we can return a second value that's status code.
    # The default is 200 (OK), so we did need to specify it before
    # Now we need to specify since it's not 200 anymore

@err.app_errorhandler(403)
def erro_403(err):
    return render_template('err_handle/err_403.html'), 403

@err.app_errorhandler(500)
def erro_500(err):
    return render_template('err_handle/err_500.html'), 500

@err.app_errorhandler(405)
def erro_405(err):
    return render_template('err_handle/err_405.html'), 405
```

Now in our templates folder, let's create a `err_handle` folder that will contain all error pages. The content of those pages will look similar like this.

```html

{% extends "layout.html" %}

{% block content %}
<div class="container">
    <h1>No Permission - 403 !</h1>
    <p>You don't have the permission to do that, check your account and try again ?</p>
</div>
{% endblock content %}
```

We can adjust the `status code` and the message accordingly
