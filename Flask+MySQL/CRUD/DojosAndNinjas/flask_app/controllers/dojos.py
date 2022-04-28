from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo # Gets all the dojos and returns them in a list of dojo objects
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos():
    dojo_list = Dojo.get_all()
    return render_template('dojos.html', dojos = dojo_list)

@app.route('/dojo/create', methods=['POST'])
def new_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name" : request.form["fname"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    Dojo.save(data)
    # print("printing data[name]" + data['name'])
    # print("printing request.form")
    # print(request.form)
    #Redirect after saving to database
    return redirect('/dojos')

@app.route('/dojos/<x>')
def dojo_ninjas(x):
    info = {
        'id' : x
    }
    intended_user = Dojo.get_dojo(info)
    ninjas = {}
    ninjas = Ninja.get_all(info)
    print("")
    return render_template('dojo_ninjas.html', intended_user = intended_user, ninjas=ninjas)

# @app.route('/ninjas')
# def ninjas():
#     dojo_list = Dojo.get_all()
#     return render_template('new_ninja.html', dojos = dojo_list)