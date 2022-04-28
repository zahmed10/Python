from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo # Gets all the dojos and returns them in a list of dojo objects

@app.route('/ninjas')
def ninjas():
    dojo_list = Dojo.get_all()
    return render_template('new_ninja.html', dojos = dojo_list)

@app.route('/add/ninja', methods=['POST'])
def new_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "dojo_selection" : request.form["dojo_selection"],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_selection"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    Ninja.save(data)
    # print("printing data[name]" + data['name'])
    # print("printing request.form")
    # print(request.form)
    #Redirect after saving to database
    return redirect(f'/dojos/{data["dojo_id"]}')