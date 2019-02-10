# Part 3: Handling Inputs

1. Now we will create a registration form for user to register. We will use extensions called WTForms, and Flask WTF which will help us so that we don't have to reinvent the whole process of creating a form and handling the validations by ourselves.

2. Install WTForms with pip by running `pip install flask-wtf` then create a new python script called `forms.py` to create forms there, also, it will keep our `run.py` clean

3. FlaskForm is a class that we will inherit from, and python will automatically convert it into HTML forms within out templates.

4. Create new class `RegistrationForm` that inherit from `FlaskForm`, inside it, we will define the form fields that we need, also we will validate the information:
  - username: string, required, maybe 50 characters long or min 2 to max 20
  - email: string, required, valid email format
  - password: password string, required
  - confirm_password: password string, required, and match with password
  - submit button

5. Create the second class `LoginForm` that also inherit from `FlaskForm` for users to log in:
  - email: string, required, valid email format
  - password: password string, required
  - remember me: boolean field
  - submit button

6. When we use this form, we need to set a secret key for our application to protect us from some basic attack such as modifying cookies and cross-site request forgery (CSRF). We can set it up in `run.py` after we instantiate the `app`.
We will use a library call `secrets` to generate a random string of secret key in Python intepreter
```python
>>> import secrets
>>> secrets.token_hex(16) # Copy the result and paste it in the config variable
```

7. Now that we have the secret key, we need to setup the form in our template. In `run.py` let's import the forms from `forms.py`

8. Create a new route for the registration `@app.route('/register')`
```python
@app.route("/register")
def register():
    form = RegistrationForm()

    return render_template("register.html", form=form)
```
Do the same thing for the LoginForm. Please note that, at this point, we have not got the `register.html` and `login.html` yet, so we will have to create those files next.

9. Create `register.html` and inherit the layout from `layout.html`
- The hidden tag `{{ form.hidden_tag() }}` must be placed in the template
- We access the form's attribute and place them in the template in {{ }}

10. If we try to fill in the form and submit it, we will get `405 Method Not Allowed`, because we have to specify the allowed methods that we are using in `/register` route. They are `GET` and `POST` requests.
```python
@app.route("/register", methods=["GET", "POST"])
```
After adding the methods, there won't be any errors, however, we haven't tell python to do anything with the submited data yet, so for now, it will redirect to `/register` page.

11. Now we will use a method to process the form after submited, in the `register()`:
```python
if form.validate_on_submit():
        username = form.username.data
        flash(f"Account created for {username} !", 'success')
        return redirect(url_for('home'))
```
- First we have to import `flash` from `flask`, to flash a message if the data has been successfully submitted or not. The first argument of `flash()` is the message that we want to display, and the second is the message bootstrap category.
- Then we all so need to import `redirect` and `url_for` from `flask` to redirect to `home.html` after submitting.

12. In order to see the flashed message, we will need to add in the `layout.html`a check command to see if there is any messages, if so, display it above the `{% block content %}`
```html
 {% with messages = get_flashed_messages(with_categories=True) %}
    {% if messages %}
      {% for category, message in messages %}
        <div class="container">
          <div class="alert alert-{{category}} mx-1">
            {{ message }}
            <button class="close" type='button' data-dismiss='alert'>
            <span>&times;</span>
            </button>
          </div>
        </div>
      {% endfor %}
    {% endif %}
  {% endwith %}
```
**However, at this stage, the data has not been saved in any databases.**

13. In case user gives invalid format or invalid data, we want to display a message to let user know what the error is. We will use bootstrap `invalid-feedback` to do this, thefore, we will have to add a conditional check in each form field. For example the username field:
```html
        <div class="form-group">
          {{ form.email.label(class="form-control-label") }}
          {% if form.email.errors %}
            {{ form.email(class="form-control form-control-lg is-invalid") }}
            <div class="invalid-feedback">
              {% for err in form.email.errors %}
                <span>{{err}}</span>
              {% endfor %}
            </div>
          {% else %}
            {{ form.email(class="form-control form-control-lg") }}
          {% endif %}
        </div>
```

14. For the `login.html` we could copy `register.html` but only keep the `email` and `password` fields

15. In the `login()` route, we will hardcode some fake data just to check if the route is working correctly:
```python
form = LoginForm()
    if form.validate_on_submit():
        admin_email = 'john@doe.com'
        admin_password = 'password'
        if form.email.data == admin_email and form.password.data == admin_password:
            flash('Log in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in failed, check credentials again', 'danger')

    return render_template("login.html", form=form)
```
16. Notice that, so far all of the `<a></a>` tags use direct link. We will change this in the next part since it is not dynamic to use direct link like that. We will refer the function names instead of the link, that way, if we restructure the app and change the link, we won't have to change them one by one in the `<a>` tags anymore
