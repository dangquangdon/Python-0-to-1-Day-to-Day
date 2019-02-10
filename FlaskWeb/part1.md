# Part 1:

1. Start new project folder and create virtual environment
2. install flask with pip `pip install flask`
3. Create a new folder for the app and `cd` into that folder
4. Create new python file `run.py`
5. Try `hello world` from flask [documentation](http://flask.pocoo.org/)
```python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

```
6. Follow the documentation and run the app
```
export FLASK_APP=run.py
flask run
```
Note: In windows, replace `export` with `set`

The app is now available in `localhost:5000`
However, when we make changes, we have to stop the server `Ctrl+C` and start it again `flask run` to see updates

7. In order to be able to see changes without shutting down server and restart it, we can set a new enviroment variable
```
export FLASK_DEBUG=1
```
Now, when we make changes, we can just refresh the page to see the changes. However, this is still not the ideal way, because if we shutdown the terminal (or command prompt), everytime when we start a new terminal to run the app, we have to repeat the `export` commands

8. We can setup in the `run.py` script so that python will take care of it. In the end of the script, add this
```python
if __name__ == "__main__":
    app.run(debug=True)
```
Then we can start the app simply by running the script `run.py`

9. Add `about` route to understand what `@app.route()` means
