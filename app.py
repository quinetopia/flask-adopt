"""Flask app for adopt app."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm




app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_homepage():
  """ Homepage """
  pets= Pet.query.all()

  return render_template("home.html", pets=pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
  """ Add a pet for adoption """
  form = AddPetForm

  if form.validate_on_submit():
    pet = Pet()
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data
    pet.age = form.age.data
    pet.notes = form.notes.data

    db.session.add(pet)
    db.session.commit()

    return redirect("/")
  
  else:
    return render_template("add_new_pet.html", form=form)