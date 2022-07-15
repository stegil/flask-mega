from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Stephen"}

    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
        },
        {
            "author": {"username": "Susan"},
            "body": "The avengers movie was so cool!",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
