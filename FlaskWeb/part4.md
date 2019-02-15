# Part 4: Database

**Since this is the learning project, we will use SQLite3 for the sake of simplicity. However, Flask can work with any database engines such as PosgreSQL, MongoDB, MySQL, etc.**

1. We are going to use [Flask_SQLAlchemy](https://www.sqlalchemy.org/), an ORM (Object Relational Mapper), it allow us to access database easily within python code in Object Oriented way. And even if we change to other database engine, we don't need to change python code except for the configuration variable.

2. `pip install flask-sqlalchemy`

3. in `run.py` import sqlalchemy and set it up
```python
from flask_sqlalchemy import SQLAlchemy

...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

db = SQLAlchemy(app)
```

4. We will make a separate file for the models later, for now, to avoid the import error, we will keep the model in `run.py`
```python
class User(db.Model):
  # In here we will add the columns for the table
  id = db.Column(db.Integer, primary_key=True)
  # In the form, we set a limit for username of maximum 20 characters
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  # for users' avatar picture, set it default.jpg
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  # The password will be hashed into a string of 60 characters
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    """ This method will printout the object in the format that we defined"""
    return f"User('{self.username}','{self.email}')"

class Post(db.Model):
  # In here we will add the columns for the table
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20), nullable=False)
  subtitle = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  # for users' avatar picture, set it default.jpg
  content = db.Column(db.Text, nullable=False)
  # The password will be hashed into a string of 60 characters

  def __repr__(self):
    """ This method will printout the object in the format that we defined"""
    return f"Post('{self.title}','{self.date_posted}')"
```

5. So now we have the models, however, the model is not completed yet. As usual, a blog post is written by someone, therefore, we will need and `author` for the post.
One user can write many posts, but a post can only have one `author`. Therefore, this is a one-to-many relationship between `Post` and `User`.
In `User`:
```python
posts = db.relationship('Post', backref='author', lazy=True)
```

In here, we set the relationship for the `User` with the `Post`, `backref` will automatically add a new column call `author` to `Post`, the `lazy` argument is basically just to query all the data at once. Because this `posts` is not an actual columns, it's actualy a additional query that runs in the background to get all the posts that this user has created.
To be able to call all the posts that a user has created, we will need an extra `user_id` column in the `Post` model
```python
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# The 'user.id' is the table name
```

6. Now we need to create the database file, so in terminal/command prompt,at this app folder, run `python shell`
```python
>>> from run import db
>>> db.create_all()
# If there is no error, means our database has been created in the project folder
# Now import the models that we've created, and create some instances
>>> from run import User, Post
>>> user_1 = User(username="John Doe", email="john@doe.com", password='password')
# note that: the id field is created automatically because it's primary key
# the image_file is also created by default value
# we will hash the password later
# to confirm the new created user
>>> db.session.add(user_1)
>>> user_2 = User(username="Jane Doe", email="jane@doe.com", password='password2')
>>> db.session.add(user_2)
# we can commit the creation of these users all at once
>>> db.session.commit()
# To see all of the users in user table
>>> User.query.all()
# To see the first one
>>> User.query.first()
# Try some query commands
>>> user = User.query.filter_by(username='John Doe').first()
>>> user.id
>>> User.query.get(2) #id number
>>> user.posts
# Create some posts
>>> post_1 = Post(title='Test 1', subtitle='Subtitle 1', content='Test content', user_id=user.id)
>>> post_2 = Post(title='Test 2', subtitle='Subtitle 2', content='Test content 2', user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
>>> post = Post.query.first()
>>> post.user_id
>>> post.author
# to delete all/drop all tables
>>> db.drop_all()
```


