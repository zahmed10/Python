from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt  

bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not User.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    # data = {
    #     "username": request.form['username'],
    # }
    data = {
        # "" : request.form["dojo_selection"],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    session['fname'] = data['fname']
    session['fname'] = data['fname']
    session['logged_in'] = True
    return redirect("/dashboard")
    # User.save(request.form)
    # return redirect("/")

@app.route('/dashboard')
def dashboard():
    # if session['logged_in'] == True and session['user_id']:
    if 'user_id' in session: # maybe add the login test session variable that was discussed here

        data = {}
        data = {
            "user_id": session['user_id'] 
        }
        fname = User.get_first_name(data)
        fname = fname[0]
        fname = fname["first_name"]
        return render_template('dashboard.html', fname = fname)
    else:
        return redirect('/')

@app.route('/logout', methods=["POST"])
def logout():
    # if request.form['logout'] == True:
    #     session.clear()
    session.clear()

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if 'logged_in' in session and session['user_id']:
        return redirect('/dashboard')
    else:
        # see if the username provided exists in the database
        data = { "email" : request.form["email"] }
        user_in_db = User.get_by_email(data)
        # user is not registered in the db
        if not user_in_db:
            flash("Invalid Email/Password")
            return redirect("/")
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Invalid Email/Password")
            return redirect('/')
        # if the passwords matched, we set the user_id into session
        session['user_id'] = user_in_db.id
        # never render on a post!!!
        return redirect("/dashboard")