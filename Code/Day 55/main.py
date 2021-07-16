from flask import Flask
import random

app = Flask(__name__)
randnum = random.randint(0, 30)


@app.route("/")
def home():
    return "<h1>Pick a number between 0 to 30</h1>" \
           "<img src='https://media.giphy.com/media/lVJvPplEQUFpe/giphy.gif' />"


print(randnum)
@app.route("/<int:numguess>")
def higherlower(numguess):
    if numguess > randnum:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/1zRfp8CgdUwzVEXSec/giphy.gif'/>"

    elif numguess < randnum:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/l2Sq5GffrCyUMEXjW/giphy.gif'/>"



if __name__ == "__main__":
    app.run(debug=True)
