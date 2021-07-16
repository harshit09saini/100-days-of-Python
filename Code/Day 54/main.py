# Introduction to Backend using Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

if __name__ == "__main__":
    app.run()