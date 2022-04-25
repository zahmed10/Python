from flask import Flask, redirect, render_template, request
# import the class from friend.pycopy
from user import User
app = Flask(__name__) 
@app.route('/users/new')
def create_user():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(debug=True)

