from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class PetForm(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                          choices=[("cat","Cat"),("dog","Dog"),("porcupine","Porcupine")],
                          validators=[InputRequired()])
    photo_url = StringField("Picture URL",
                            validators=[Optional(),URL("Please input a valid URL")])
    age = FloatField("Age",
                     validators=[Optional(),NumberRange(0,30, "Age must be between 0 and 30")])
    notes = StringField("Notes",
                        validators=[Optional()])
