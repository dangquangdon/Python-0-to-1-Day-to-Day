# Part 10: Migration and Deployment

## Migration

As many of you might have notice, since we moved our files to blueprints, we are unable to access the database from command line anymore.

In this part, we will implement some small changes and add data migrations.

1. in `config/dev.py` let's adjust the location of our database `flaskapp.db`, by changing the environment variable:

```python
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.join(os.getcwd(),"flaskapp.db")}'
```

After this, delete the old database file, hopefully you don't have anything too important there.

2. In your `run.py`, first let's change the name of the script to `manage.py`. Open the terminal or command prompt, and install two new extensions:

- `pip install flask-migrate`

- `pip install flask-script`

Then in `manage.py`, let's adjust the content

```python
from app import db, create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('dev')
with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate = Migrate(app, db, render_as_batch=True)
    else:
        migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__=="__main__":
    manager.run()
```

Flask Migrate will be the version control of your database from now on. If you make any changes such as add columns, modify columns' names and so on, you don't need to delete the old one and create a new one anymore.

Flask Script will give you some more command, we will go through some basic commands together.

3. After the two step above, now you can open your terminal/command prompt, activate your virtualenv and type

`python manage.py` and press `Enter`. You will see that Flask will give you thee options: - `db` to perform database migrations

- `shell` to activate python interpreter inside Flask application context - `runserver` to run flask app

Since we already deleted our old database file, before we can start the app, we have to create a new one.

- run `python manage.py db init`, it will create a folder `migrations` which will store all versions of your database. **only run in the first time**
- next `python manage.py db migrate`, it will start migrating and push the changes to staging area (sound familiar?)
- last `python manage.py db upgrade`, your changes will be taken effect, the new database file will be created if this is the first time running.

Now if you want to start your server, run `python manage.py runserver`

If you want to access your database from terminal and practicing the Flask_SQLAlchemy syntax, run `python manage.py shell` and start importing `User` or `Post` and play around with it

4. From now on, everything you make any changes such as add new tables or columns in your database, you can start runing
   - `python manage.py db migrate`
   - then `python manage.py db upgrade`

## Deployment

To be updated !
