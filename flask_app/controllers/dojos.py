from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def homepage():
    return redirect("/dojos")

@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos = dojos)

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")



# @app.route("/dojos/<int:id>")
# def show(id):
#     ninjas = Ninja.get_all()
#     data = {
#         "id":id
#     }
#     return render_template("dojo_show.html",)

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template("dojo_show.html", dojo=Dojo.dojo_students(data))



