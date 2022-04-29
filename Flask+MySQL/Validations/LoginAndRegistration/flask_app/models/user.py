from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# from flask_app import app
# from flask_bcrypt import Bcrypt  
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
#                         # which is made by invoking the function Bcrypt with our app as an argument



class User:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.fname = db_data['first_name']
        self.lname = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.added_at = db_data['added_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.users = []
    
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_registration').query_db(query)
        print(results) # Debugging purposes and to understand what is in results
        # On inspecting the output of the previous line, results is a list of dictionaries
        # Create an empty list to append our instances of dojos
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
        
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO users ( first_name , last_name, email, password, added_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('login_registration').query_db(query,data)

    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['fname']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(burger['lname']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(burger['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        if len(burger['password']) < 3:
            flash("Password must be at least 3 characters.")
            is_valid = False
        # if len(burger['meat']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(burger['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_first_name(cls, data):
        query = "SELECT first_name FROM users WHERE id = %(user_id)s"
        # "INSERT INTO users ( first_name , last_name, email, password, added_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('login_registration').query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])