from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "962bc0a64ccb9095bb01144dcbfbb2c6"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

movie = None


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True)
    year = db.Column(db.Integer())
    description = db.Column(db.Text())
    rating = db.Column(db.Float())
    ranking = db.Column(db.Integer())
    review = db.Column(db.Text())
    img_url = db.Column(db.String(50))

    def __repr__(self):
        return f"<Movie {self.title}"


db.create_all()


class EditForm(FlaskForm):
    rating = StringField(label="Rating", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Edit Movie")


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie = form.title.data
        # Send API REQUEST

        params = {
            "api_key": API_KEY,
            "query": movie,
        }
        movie_request = requests.get('https://api.themoviedb.org/3/search/movie', params=params)
        movie_request.raise_for_status()
        return render_template("select.html", movies_response=movie_request.json()["results"])
    return render_template("add.html", form=form)

@app.route("/add/<id>")
def movie_details(id):
    movie_details_request = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}')
    movie_details_request.raise_for_status()
    movie_data = movie_details_request.json()
    new_movie = Movie(
        title=movie_data['title'],
        year=movie_data['release_date'].split('-')[0],
        description=movie_data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()

    movie_added = Movie.query.filter_by(title=new_movie.title).first()
    return redirect(url_for("edit", id=movie_added.id))

@app.route("/edit/<id> ", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    movie_to_edit = Movie.query.get(id)
    if form.validate_on_submit():
        print(form.rating.data)
        print(form.review.data)
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route("/delete/<id>")
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
