from app.auth import auth
from flask import Flask, render_template, url_for, flash, redirect
from app.auth.forms import LoginForm, RegistrationForm
from app import bcrypt, db
from app.auth.models import User
from flask_login import login_user, current_user


@auth.route("/register", methods=["GET", "POST"])
def register():
    # Check if the user is already logged in
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('posts.home'))

    # if not logged in
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=username,
                        email = form.email.data,
                        password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Account created for {username} !", 'success')
        return redirect(url_for('posts.home'))

    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        input_password = form.password.data
        if user and bcrypt.check_password_hash(user.password, input_password):
            login_user(user, remember=form.remember.data)
            flash('Log in successfully', 'success')
            return redirect(url_for('posts.home'))
        else:
            flash('Log in failed, check credentials again', 'danger')

    return render_template("login.html", form=form)
