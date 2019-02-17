from app.posts import posts
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from app.posts.forms import PostForm
from app.posts.models import Post
from app import db

# HOME
@posts.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)

    return render_template("home.html", posts=posts)

# ADD POST
@posts.route('/post/add-new', methods=['GET','POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    subtitle = form.subtitle.data,
                    content = form.content.data,
                    author = current_user)

        db.session.add(post)
        db.session.commit()

        flash('Post has been created!', 'success')
        return redirect(url_for('posts.home'))
    return render_template('add_post.html', form=form, form_title="Add a new post")

# VIEW A SINGLE POST
@posts.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

# EDIT A POST
@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Check if the current user is the author of the post
    if post.author != current_user:
      abort(403) #http response for forbidden route

    form = PostForm()
    if request.method == "GET":
        form.title.data = post.title
        form.subtitle.data = post.subtitle
        form.content.data = post.content

    elif form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.content = form.content.data

        db.session.commit()
        flash("This post has been updated!", 'success')
        return redirect(url_for('posts.single_post', post_id=post.id))

    return render_template('add_post.html', form=form, form_title="Edit Post")


# DELETE A POST
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash("Your post has been deleted!", 'success')
    return redirect(url_for('posts.home'))

