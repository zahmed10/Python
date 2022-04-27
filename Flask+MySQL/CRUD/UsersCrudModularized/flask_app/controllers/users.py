# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

from flask_app.models.user import User
# gets all the burgers and returns them in a list of burger objects .

@app.route('/users/new')
def create_user():
    return render_template('adduser.html')

@app.route('/process/user', methods=['POST'])
def process_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    # print(request.form)
    return redirect('/users')

@app.route('/users')
def show_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template('showusers.html', all_users = users)

@app.route('/users/<x>') # @app.route('/users/one_user.id')
def oneUser(x):
    info = {
        'id' : x
    }
    intended_user = User.get_user(info)
    print("")
    return render_template('userpage.html', intended_user = intended_user)

@app.route('/users/<y>/edit')
def editUser(y):
    info = {}
    info = {
        'id' : y
    }
    intended_user = User.get_user(info)
    return render_template('edituser.html', intended_user = intended_user)

@app.route('/process/edits', methods=['POST'])
def processEdits():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data3 = {
        "id": request.form["hidden_id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.update(data3)
    # Don't forget to redirect after saving to the database.
    # print(request.form)
    return redirect('/users')

@app.route('/users/<z>/delete')
def deleteUser(z):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data2 = {
        "id" : z
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.delete(data2)
    # Don't forget to redirect after saving to the database.
    # print(request.form)
    return redirect('/users')