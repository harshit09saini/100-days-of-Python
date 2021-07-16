from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=8, max=35)])
    submit = SubmitField(label='Submit')


