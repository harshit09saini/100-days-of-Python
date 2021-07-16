import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_response = requests.get("https://jsonplaceholder.typicode.com/posts")
blog_response.raise_for_status()
posts = blog_response.json()

post_objects = []
for post in posts:
    post_object = Post(post["id"], post["title"], post["body"])
    post_objects.append(post_object)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/posts/<post_id>')
def post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == int(post_id):
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
