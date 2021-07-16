from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Location URL (Google Maps URL)', validators=[DataRequired(), URL(message="Enter a valid URL")])
    open = StringField(label='Opening Hours (For Example: 8AM)', validators=[DataRequired()])
    close = StringField(label='Closing Hours (For Example: 8PM)', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating',
                         choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                         validators=[DataRequired()])
    wifi = SelectField(label='WiFi Rating',
                       choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'],
                       validators=[DataRequired()])
    outlets = SelectField(label='Power Outlets',
                          choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌',
                                   '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField(label='Submit')
