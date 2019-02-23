# Part 2: Templating

1. Instead of returning a string, we can also return html tags.
```python
....
  return """
  <html>
    <head></head>
    <body></body>
    ....
  </html>
  """
  ```
  However, doing that for every single route is not good at all. Therefore, we will need a templates folder and we can create HTML files there and render them to the screen.

2. After creating the templates folder, and creating `home.html`, in the `run.py` we can do the following:
    - import `render_tempalte` from `flask`
    - use `render_template`
    ```python
    ....
      return render_template("home.html")
    ```
3. We can do the same for other routes.
4. Before creating a database to store data, let's use some dummy data to see how we can pass the data from python to display in the browser
5. Create some dummy data before the `@app.route()`
```python
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
```

6. To pass data to the template, we can simply pass it in the `render_template()` as the second argument.
```python
return render_template("home.html", posts = posts)
```

7. We can access to the data from the template. Flask uses Jinja2 as templating engine, and we can write codes that quite similar to python in the html files.
```html
{% for post in posts %}
  <h1>{{ post.title }}</h1>
  <p>{{ post.author }}</p>
  <p>{{ post.content }}</p>
{% endfor %}
```
We can also add `{% if %}` and `{% else %}` statements as well. We can modify the above code:
```html
{% if posts %}
  {% for post in posts %}
    <h1>{{ post.title }}</h1>
    <p>{{ post.author }}</p>
    <p>{{ post.content }}</p>
  {% endfor %}
{% else %}
  <p>No posts</p>
{% endif %}
```

## Template inheritance

8. Jinja2 allow us to inherit the template from a single template, so that we don't have to retype the common areas of the page again, for example the navbar, the head section, the footer and so on. In this example, we will create a new html file and set it as them base layout for the whole page, let's call it `layout.html`

9. In the `layout.html`, we code down all of the common area, and in the `<body>` tag, we create a block with this syntax:
  ```html
  {% block content %}
    <!-- Content goes here -->
  {% endblock %}
  ```
  With Jinja2, we can create some empty blocks like this, in this case, I call this block `content`, however, you can name it anything, but let's do so that it makes sense when you read it.

10. Now in the `home` and `about` page, we can delete all the common area, and inherit the layout as following:
```html
{% extends "layout.html" %}
{% block content %}
  <h1>About</h1>
  {% if posts %}
    {% for post in posts %}
      <h1>{{ post.title }}</h1>
      <p>{{ post.author }}</p>
      <p>{{ post.content }}</p>
    {% endfor %}
  {% else %}
    <p>No posts</p>
  {% endif %}
{% endblock content%}
```

11. To see more about the benefit of using template inherit, we can style out page a bit now, I will use [bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) for simplicity

12. We can also add our own css by creating `static` folder.

