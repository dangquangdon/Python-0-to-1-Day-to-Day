from app.posts import posts
from flask import Flask, render_template

@posts.route("/")
def home():
    return render_template("home.html")

@posts.route("/about")
def about():
    return render_template("about.html")
