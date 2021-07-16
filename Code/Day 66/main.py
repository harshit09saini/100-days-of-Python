import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        print(self.id)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return jsonify({"id": random_cafe.id,
                    "name": random_cafe.name,
                    "map_url": random_cafe.map_url,
                    "img_url": random_cafe.img_url,
                    "location": random_cafe.location,
                    "seats": random_cafe.seats,
                    "has_toilet": random_cafe.has_toilet,
                    "has_wifi": random_cafe.has_wifi,
                    "has_sockets": random_cafe.has_sockets,
                    "can_take_calls": random_cafe.can_take_calls,
                    "coffee_price": random_cafe.coffee_price})


@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    all_cafes = []
    for cafe in cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        all_cafes.append(cafe_dict)
    return jsonify(cafes=all_cafes)


@app.route("/search")
def search_all():
    location = request.args.get('loc').title()
    print(location)

    search_cafe = Cafe.query.filter_by(location=location).first()
    print(search_cafe)
    try:
        cafe_dict = {
            "id": search_cafe.id,
            "name": search_cafe.name,
            "map_url": search_cafe.map_url,
            "img_url": search_cafe.img_url,
            "location": search_cafe.location,
            "seats": search_cafe.seats,
            "has_toilet": search_cafe.has_toilet,
            "has_wifi": search_cafe.has_wifi,
            "has_sockets": search_cafe.has_sockets,
            "can_take_calls": search_cafe.can_take_calls,
            "coffee_price": search_cafe.coffee_price
        }
    except AttributeError:
        return jsonify(Error="No Cafes found at the given location")
    return jsonify(cafes=cafe_dict)
    ## HTTP POST - Create Record


@app.route('/add', methods=["POST"])
def add_cafe():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("location"),
                    seats=request.form.get("seats"),
                    has_toilet=bool(request.form.get("toilets")),
                    has_wifi=bool(request.form.get("wifi")),
                    has_sockets=bool(request.form.get("sockets")),
                    can_take_calls=bool(request.form.get("calls")),
                    coffee_price=request.form.get("price"),
                    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully added the new cafe"
    })
    ## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
    try:
        cafe_to_update.coffee_price = new_price
    except AttributeError:
        return jsonify(response={
            "error": "Cafe Not Found."
        }), 404
    db.session.commit()
    return jsonify(response={
        "success": "Successfully updated the price."
    })

    ## HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "66060f696feff26a0bfd8a1234ef9d":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
