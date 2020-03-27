"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, 
from wtforms.validators import InputRequired, URL

class AddPetForm(FlaskFrom):
  """Form for adding a pet to adopt."""
  name = StringField("Pet name:", validators=[InputRequired()])
  species = StringField("Species:", validators=[InputRequired()])
  photo_url = StringField("URL for a picture:", validators=[URL(require_tld=true, message ="Sorry, we can unly accept URL's from external websites")])
  age = SelectField("Age:", 
    choices=[("baby", "baby"),("young", "young"),
     ("adult", "adult"), ("senior", "senior")])
  notes = TextAreaField("Notes:")