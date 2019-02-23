# Part 8: Posts

Now that we have done pretty much with the user authentication, we will start working on posts.

## Create Post

1. In the `posts/routes.py` let's create a basic route for adding new post.

```python
from flask_login import login_required

@posts.route('/post/add-new')
@login_required
def add_post():
  return render_template('add_post.html')

```

2. Before creating the `add_post.html`, let's create a form for user to write posts. So in `posts/forms.py`

```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')
```

3. Now we have to import this form to the `posts/routes.py` and put it the usual validate on submit and flash a message to see if it's working.

```python
from app.posts.forms import PostForm

...
@posts.route('/post/add-new', methods=['POST', "GET"])
@login_required
def add_post():
  form = PostForm()
  if form.validate_on_submit():
    flash('Post has been created!' , 'success')
    return redirect(url_for('posts.home'))
  return render_template('add_post.html', form=form)
```

4. Let's create the `add_post.html` file in the `templates` so that we can check if it's working

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="row">
    <div class="col-sm-9 mx-auto pt-3">
      <div class="text-center">
        <h1>Add new post</h1>
      </div>
      <form method="POST">
        <!-- This hidden form is to protect us from CSRF attack -->
        {{ form.hidden_tag() }}
        <div class="form-group">
          {{ form.title.label(class="form-control-label") }}
          {% if form.title.errors %}
            {{ form.title(class="form-control form-control-lg is-invalid") }}
            <div class="invalid-feedback">
              {% for err in form.title.errors %}
                <span>{{err}}</span>
              {% endfor %}
            </div>
          {% else %}
            {{ form.title(class="form-control form-control-lg") }}
          {% endif %}
        </div>
        <div class="form-group">
          {{ form.subtitle.label(class="form-control-label") }}
          {% if form.subtitle.errors %}
            {{ form.subtitle(class="form-control form-control-lg is-invalid") }}
            <div class="invalid-feedback">
              {% for err in form.subtitle.errors %}
                <span>{{err}}</span>
              {% endfor %}
            </div>
          {% else %}
            {{ form.subtitle(class="form-control form-control-lg") }}
          {% endif %}
        </div>
        <div class="form-group">
          {{ form.content.label(class="form-control-label") }}
          {% if form.content.errors %}
            {{ form.content(class="form-control form-control-lg is-invalid") }}
            <div class="invalid-feedback">
              {% for err in form.content.errors %}
                <span>{{err}}</span>
              {% endfor %}
            </div>
          {% else %}
            {{ form.content(class="form-control form-control-lg") }}
          {% endif %}
        </div>
        <div class="form-group">
          {{ form.submit(class="btn btn-outline-info") }}
        </div>
      </form>
    </div>
  </div>
{% endblock %}
```
Also, let's add the `Add Post` to the main navbar

5. To save the post the the database, it's fairly simple and similar to save newly registered users, except that we don't have to hash anything here.

```python
from flask import current_user
...
  if form.validate_on_submit():
    post = Post(title= form.title.data,
                subtitle = form.subtitle.data,
                content = form.content.data,
                author = current_user)

    db.session.add(post)
    db.session.commit()
    ...
```

6. Now back to the `home` route

```python
@posts.route("/")
def home():
  posts = Post.query.all()

  return render_template("home.html", posts=posts)
```

7. Let's also adjust the `home.html`

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container">
    {% if posts %}
      {% for post in posts %}
        <div class="row box p-3 bg-primary my-2 text-white">
          <div class="col-sm-8">
            <h1><a href="{{url_for('posts.single_post', post_id=post.id)}}" class="text-white">
              {{ post.title }}
            </a>
            </h1>
            <h3>{{post.subtitle}}</h3>
            <p>{{ post.author.username }}</p>
            <small>{{post.date_posted.strftime('%Y-%m-%d')}}</small>
          </div>
          <div class="col-sm-4">
            <img src="{{ url_for('static', filename='img/profile_pics/'+post.author.image_file) }}">
          </div>
        </div>
      {% endfor %}
    {% else %}
      <p>No posts</p>
    {% endif %}
  </div>
{% endblock content %}
```

8. Now let's create a route so that user can access one single post to read it.

```python
@posts.route('/post/<post_id>')
def single_post(post_id):
  post = Post.query.get_or_404(post_id)

  return render_template('post.html', post=post)
```

9. Now create a new `post.html` file

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container">
    <div class="row box p-3 bg-primary my-2 text-white">
      <div class="col-sm-8">
        <h1>{{ post.title }}</h1>
        <h3>{{post.subtitle}}</h3>
        <p>{{ post.author.username }}</p>
        <p>{{ post.content }}</p>
        <small>{{post.date_posted.strftime('%Y-%m-%d')}}</small>
      </div>
      <div class="col-sm-4">
        <img src="{{ url_for('static', filename='img/profile_pics/'+post.author.image_file) }}">
      </div>
    </div>
  </div>
{% endblock content %}
```

## Edit Post

10. Now we will add a new function to edit the existing post. In the `posts/routes.py` let's add a new route to update/edit posts

```python
from flask import abort

@posts.route('/post/<post_id>/update')
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Check if the current user is the author of the post
    if post.author != current_user:
      abort(403) #http response for forbidden route

    form = PostForm()
    return render_template('add_post.html', form=form)
```
You might think that we will need to create a new `html` file in the templates folder for it, but since it's going to look exactly the same as the `add_post.html`, we are going to use `add_post.html`. The only thing we need to modify is the title of the form. If in `add_post` route, the form field title is "Add new post", now in the `edit_post` route, it should be "Edit Post" or something like that.

To do that, we will give it a variable for both routes, and change the value accordingly.

- In `add_post` route
```python
return render_template('add_post.html', form=form, form_title="Add a new post")
```

- In `edit_post` route
```python
return render_template('add_post.html', form=form, form_title="Edit Post")
```

11. So we want to populate the form fields with the current data of the post, the process will be very similar as we did for the `Account` page when we want to update user's information. So the complete `edit_post` route is:

```python
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
```

## Delete Post

12. Now we want to add a function to delete the post. Before that, let's add some buttons for users to go to `edit_post` route or `delete_post` route. So in the `post.html` let's add some coditional check

```html
{% extends 'layout.html' %}
{% block content %}
  <div class="container">
    <div class="row">
      <div class="col-sm-8 box p-3 bg-primary my-2 text-white">
        <h1>{{ post.title }}</h1>
        <h3>{{post.subtitle}}</h3>
        <p>{{ post.author.username }}</p>
        <small>{{post.date_posted.strftime('%Y-%m-%d')}}</small>
        <p>{{ post.content }}</p>
      </div>
      <div class="col-sm-4 p-3 my-2">
        <div class="row mx-auto justify-content-center">
          <img src="{{ url_for('static', filename='img/profile_pics/'+post.author.image_file) }}">
        </div>
        {% if post.author == current_user %}
          <div class="row mx-auto justify-content-center">
            <a class="btn btn-secondary m-1" href="{{url_for('posts.edit_post', post_id=post.id)}}">Edit</a>
            <button type="button" class="btn btn-danger m-1" data-toggle='modal' data-target="#deleteModal">Delete</button>
          </div>
        {% else %}
        {% endif %}
      </div>
    </div>
  </div>
{% endblock content %}
```

Usually, when users click to delete, we need to make sure they don't do that accidentally, so we want to ask again if they're sure they want to delete it. So we are going to use [Bootstrap 4 Modal](https://getbootstrap.com/docs/4.0/components/modal/). So outside of the first level `<div class="container">`, right above the `{% endblock content %}`, we can add the modal.

```html
<div class="modal fade" id="deleteModal" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Post</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Are you sure you want to delete this post ?</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
          <form action="{{url_for('posts.delete_post', post_id=post.id)}}" method="POST">
            <input type="submit" class="btn btn-danger" value="Delete">
          </form>
        </div>
      </div>
    </div>
  </div>
```

As you might have notice, the delete button is actually a submit input wrapped inside a `<form>` tag. The action of the `<form>` is the `delete_post` that we are going to create after this. The reason we put it in `<form>` tag because, the `delete_post` is going to be a `POST` request.

13. Now let's create the `delete_post` route. In the `posts/routes.py`

```python
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
```
