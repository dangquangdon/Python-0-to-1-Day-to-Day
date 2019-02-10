from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'c0a254194d6c4a955187cf4a27e221af'

posts = [
  {
    'author':'Don',
    'title': "Test post 1",
    'content': "Test content 1"
  },
  {
    'author':'Don',
    'title': "Test post 2",
    'content': "Test content 2"
  },
  {
    'author':'Don',
    'title': "Test post 3",
    'content': "Test content 3"
  },
]


@app.route("/")
def home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        flash(f"Account created for {username} !", 'success')
        return redirect(url_for('home'))

    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
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


if __name__ == "__main__":
    app.run(debug=True)
