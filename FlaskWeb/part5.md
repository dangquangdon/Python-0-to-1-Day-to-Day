# Part 5: Restructure the project directory using `Blueprint`

We will restructure this app into a package

1. create `models.py` and move all the models to it, and do the importing, and run app to check if it works

2. The error that we have is called `circular imports` in python.
- Basically, when we run the script, it execute from top down.
- For python, when it imports a module, it actually runs that module rightaway. We might think that we haven't execute the code yet, but actually python already start executing the modules while importing them.
- So it comes to the `from models import User, Post` and execute the `models.py`
- In the `models.py` we `from run import db`, then python goes back to `run.py` and start runing from the begining again and never found `db`
- A work-around for this issue is to put `from models import User,Post` below `db = SQLAlchemy(app)`. It will work, however, this way make the code "ugly"

3. We want to keep the files separately in order to keep the code clean and maintainable, therefore, we will turn this app into a package. And to do so, we need to have an `__init__.py` file

4. In the project folder, create a new folder named `app`, and in `app`, create a `__init__.py` file

5. Move `static` and `templates` folders into `app` folder

6. We are going to separate the routes in `run.py` into different folders, `auth` for user and user authentication, `posts` for all the posts related.

7. In `auth` and `posts` both, we will create these files below:
- `__init__.py`
- `models.py`
- `forms.py`
- `routes.py`

8. Then we start split the original `forms.py` and `models.py` accordingly

9. Start with the `auth`, in the `__init__.py`, we start the blueprint
```python
from flask import Blueprint

auth = Blueprint('auth', __name__)

from app.auth import routes
```
10. Bring all the necessary imports and `User` class to `models.py`

11. Bring all the necessary imports, `LoginForm` and `RegisterForm` classes to `forms.py`

12. Outside the `app` folder, create a new folder called `config` to store the configuration variables. In the `config` folder, create two new files `dev.py` and `prod.py` to store to different configuration settings for development environment and production environment.

13. Rewrite the `__init__.py` in `app` folder

14. Rewrite the `run.py`

15. There are probably erros, let's run the app to findout and fix them
