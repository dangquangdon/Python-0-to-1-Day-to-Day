from app.auth import auth
from flask import Flask, render_template, url_for, flash, redirect
from app.auth.forms import LoginForm, RegistrationForm
from app import bcrypt, db
from app.auth.models import User


@auth.route("/register", methods=["GET", "POST"])
def register():
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
    form = LoginForm()
    if form.validate_on_submit():
        admin_email = 'john@doe.com'
        admin_password = 'password'
        if form.email.data == admin_email and form.password.data == admin_password:
            flash('Log in successfully', 'success')
            return redirect(url_for('posts.home'))
        else:
            flash('Log in failed, check credentials again', 'danger')

    return render_template("login.html", form=form)
