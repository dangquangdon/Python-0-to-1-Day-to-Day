from app.auth import auth
from flask import Flask, render_template, url_for, flash, redirect, request
from app.auth.forms import LoginForm, RegistrationForm, UpdateAccount
from app import bcrypt, db
from app.auth.models import User
from flask_login import login_user, current_user, logout_user, login_required
from app.auth.utils import save_picture

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
        return redirect(url_for('auth.login'))

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
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('posts.home'))
        else:
            flash('Log in failed, check credentials again', 'danger')

    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('posts.home'))

@auth.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        pic_data = form.picture.data
        if pic_data:
            picture_name = save_picture(pic_data)
            current_user.image_file = picture_name

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account has been updated!", 'success')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', form=form)
