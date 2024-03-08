"""Pet Adoptions application"""

from flask import Flask, request, redirect, render_template, flash, get_flashed_messages
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home():
    """Home page"""

    all_pets = Pet.query.all()

    return render_template("home.html",pets=all_pets)

@app.route("/add", methods=["GET","POST"])
def add_pet():
    """Add new pet"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else None
        age = form.age.data
        notes = form.notes.data

        newPet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(newPet)
        db.session.commit()
        flash(f"Added the {species} {name}")
        return redirect("/")
    else:
        return render_template("pet_form.html",form=form)

@app.route("/edit_pet/<int:petid>",methods=["GET","POST"])
def edit_pet(petid):
    """Show edit pet form and handle edit"""

    pet = Pet.query.get_or_404(petid)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        flash(f"{pet.name} updated!")
        return redirect("/")
    
    else:
        return render_template("pet_form.html",form=form)
