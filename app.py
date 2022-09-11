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
from datetime import datetime

date = datetime.now()
p = Post('Test', 'Testing Content', date)
print(p.__repr__)
expected = f'<bound method Post.__repr__ of Post<0,Test,{date},Testing Content>>'
print(expected)


posts1 = Post.add_post("Test Post", "This is my awsome text.")
posts2 = Post.add_post("Test Post2", "This is my awsome text.")
print(posts1)
print(posts2.__repr__)

