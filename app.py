"""Flask app for adopt app."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


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
  form = AddPetForm()

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

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_pet_details(pet_id):
    """ shows bio for pet in question """
    # debugger()
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f"/{pet_id}")

    else:
        return render_template("display_pet.html", pet=pet, form=form)

