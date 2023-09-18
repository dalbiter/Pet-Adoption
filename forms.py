from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name cannot be blank")])
    species = SelectField("Species", validators=[InputRequired(message="Species cannot be blank")])
    photo_url = URLField("Photo URL", validators=[Optional()])
    age = IntegerField("Age")
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = URLField("Photo URL", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = SelectField("Available", validators=[InputRequired()], choices=[('t', 'Available'), ('f', 'Recently Adopted')], coerce=lambda x: x == 'True')
    