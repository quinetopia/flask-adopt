"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

# def approved_species(form, field):
#     ok = ['dog', 'cat', 'porcupine']


class AddPetForm(FlaskForm):
    """Form for adding a pet to adopt."""
    name = StringField("Pet name:", validators=[InputRequired()])
    species = SelectField(
                          "Species:",
                          choices=[('dog', 'dog'),
                                   ('cat', 'cat'), ('porcupine', 'porcupine')],
                          validators=[InputRequired()])
    photo_url = StringField("URL for a picture:",
                            validators=[Optional(),
                                        URL(require_tld=True,
                                        message="""Sorry, we can unly accept
                                                URL's from external websites""")])
    age = IntegerField("Age:",
                       validators=[NumberRange(min=0, max=30,message="Please enter an age between 0 and 30")])
    notes = TextAreaField("Notes:")


class EditPetForm(FlaskForm):
    """ Form for editing pet information """
    photo_url = StringField("URL for a picture:",
                            validators=[Optional(),
                                        URL(require_tld=True,
                                        message="""Sorry, we can unly accept
                                                URL's from external websites""")])
    notes = TextAreaField("Notes:")
    available = BooleanField("Available", validators=[InputRequired()])
