# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the restaurant table from our database
from flask_app.models import ninja
class Dojo:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # We create a list so that later we can add in all the ninjas that are associated with a dojo.
        self.ninjas = []
    
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results) # Debugging purposes and to understand what is in results
        # On inspecting the output of the previous line, results is a list of dictionaries
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
        
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        user_info = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(user_info[0])
    # @classmethod
    # def get_dojo_id( cls, data ):
    #     query = "SELECT id FROM dojos WHERE id = "