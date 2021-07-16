from flask import Flask, render_template, request
from forms import contactForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"] = 'ebdc58f390f719d3882c07661dba32a5'

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = contactForm()
    if form.validate_on_submit():
        if form.name.data == "Harshit" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)