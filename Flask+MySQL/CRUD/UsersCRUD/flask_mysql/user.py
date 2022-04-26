# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user_info = connectToMySQL('users_schema').query_db(query, data)
        return cls(user_info[0])

    
    # ... other class methods
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s"
        connectToMySQL('users_schema').query_db( query, data)

    @classmethod
    def update(cls, data ):
        if (data['fname'] == '' and data['lname'] != '' and data['email'] != ''):
            query = "UPDATE users SET last_name= %(lname)s, email = %(email)s WHERE id = %(id)s"
        elif (data['fname'] != '' and data['lname'] == '' and data['email'] != ''):
            query = "UPDATE users SET first_name = %(fname)s, email = %(email)s WHERE id = %(id)s"
        elif (data['fname'] != '' and data['lname'] != '' and data['email'] == ''):
            query = "UPDATE users SET first_name = %(fname)s, last_name= %(lname)s WHERE id = %(id)s"

        elif (data['fname'] != '' and data['lname'] != '' and data['email'] != ''):
            query = "UPDATE users SET first_name = %(fname)s, last_name= %(lname)s, email = %(email)s WHERE id = %(id)s"

        elif (data['fname'] != '' and data['lname'] == '' and data['email'] == ''):
            query = "UPDATE users SET first_name = %(fname)s WHERE id = %(id)s"
        elif (data['fname'] == '' and data['lname'] != '' and data['email'] == ''):
            query = "UPDATE users SET last_name= %(lname)s WHERE id = %(id)s"
        elif (data['fname'] == '' and data['lname'] == '' and data['email'] != ''):
            query = "UPDATE users SET email = %(email)s WHERE id = %(id)s"

        elif (data['fname'] == '' and data['lname'] == '' and data['email'] == ''):
            query = ""
        
        else:
            print("Invalid input")


        # query = "UPDATE users SET first_name = %(fname)s, last_name= %(lname)s, email = %(email)s WHERE id = %(id)s"
        # first_name = %(fname)s AND last_name = %(lname)s AND email = %(email)s"
        connectToMySQL('users_schema').query_db( query, data)