from app.auth import auth
from flask import Flask, render_template, url_for, flash, redirect, request
from app.auth.forms import (LoginForm, RegistrationForm,
                            UpdateAccount, RequestForm,
                            ResetPasswordForm)
from app import bcrypt, db
from app.auth.models import User
from flask_login import login_user, current_user, logout_user, login_required
from app.auth.utils import save_picture
from app.posts.models import Post
from app.auth.utils import send_reset_email

# REGISTER
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

# LOGIN
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


# ACCOUNT PAGE
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


# USER'S POSTS
@auth.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    # User backslash to break the code into lines
    posts = Post.query.filter_by(author=user)\
                    .order_by(Post.date_posted.desc())\
                    .paginate(page=page, per_page=1)

    return render_template("user_post.html", posts=posts, user=user)

# RESET PASSWORD
@auth.route('/reset-password', methods=['GET','POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('posts.home'))

    form = RequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash('An email has been send to your email, please follow the instruction', 'info')
        return redirect(url_for('auth.login'))
    return render_template('reset_request.html', form=form)

# RESET TOKEN
@auth.route('/reset-password/<token>', methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('posts.home'))

    user = User.verify_reset_token(token)

    if not user:
        flash('Request has been expired, make a new request now', 'warning')
        return redirect(url_for('auth.reset_password'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user.password = hashed_password
        db.session.commit()
        flash(f"Password has been reset for {user.username} !", 'success')
        return redirect(url_for('auth.login'))

    return render_template('reset_token.html', form=form)
