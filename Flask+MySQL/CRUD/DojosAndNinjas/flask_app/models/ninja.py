from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age, created_at, updated_at, dojo_id ) VALUES (%(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results) # Debugging purposes and to understand what is in results
        # On inspecting the output of the previous line, results is a list of dictionaries
        # Create an empty list to append our instances of dojos
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas