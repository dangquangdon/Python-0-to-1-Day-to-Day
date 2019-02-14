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

5. Now we can let an user to register and the data is stored in database. However, we have to implement a check to make sure this user has already registered or not, or else SQLAlchemy will throw errors
```python

