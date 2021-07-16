import requests
from flask import Flask, render_template, request

app = Flask(__name__)

post_request = requests.get("https://jsonplaceholder.typicode.com/posts").json()


@app.route("/")
def home():
    return render_template("index.html", blogs=post_request)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        contact_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "message": request.form["message"]
        }
        print(contact_data)
        return render_template("contact.html", sent=True)
    else:
        return render_template("contact.html", sent=False)


@app.route("/posts/<post_id>")
def post(post_id):
    print(post_id)
    for blog in post_request:
        if(blog["id"] == int(post_id)):
            requested_post = blog
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)

