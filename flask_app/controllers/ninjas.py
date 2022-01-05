from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.models import dojo, ninja 

@app.route("/ninjas")
def new():
    return render_template("ninja.html", dojos= Dojo.get_all())

@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/')
