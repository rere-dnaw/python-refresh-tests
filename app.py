# from flask import Flask, redirect, url_for, render_template


# app = Flask(__name__)


# @app.route("/")
# def home_page():
#     return render_template("index.html")

# @app.route("/<name>")
# def user_name(name):
#     return f"Hello {name}!"

# @app.route("/admin")
# def admin_page():
#     return redirect(url_for("user_name", name="Admin"))



# if __name__ == "__main__":
#     app.run(debug=True)

from post import Post
from blog import Blog
from datetime import datetime

b = Blog("Cars", "Tom Don")

#b.posts.append(Post('Fiat New', 'New content info.'))


print(b.json())
