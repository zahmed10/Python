# import the class from friend.pycopy
from flask_app import app
from flask_app.controllers import users
# ...server.py




if __name__ == "__main__":
    app.run(debug=True)


# Think of as html is the starting point, follow the route to the controller, a controller has matching route where method
# does some logic. Create, read, update, delete, anything. CRUD call on class method with data provided. Class method will work
# with data and return a proper response. Take that response, send it to the html. HTML is starting point more for forms.

# Setting up modularization
# Flask app folder
# Controllers all the directories 
# init.py
# server.py
# Create controller files
# Templates to be rendered
# Controllers - index route - render index html - to make sure modularization went correctly and then from there assignment