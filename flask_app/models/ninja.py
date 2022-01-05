from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)
    #   first_name in query refers to schema..blue code refers
    
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL("dojos_and_ninjas").query_db(query)
        ninjas = []
        for x in result:
            ninjas.append( cls(x) )
        return ninjas
    
    # @classmethod
    # def new(cls, data):
    #     query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,) VALUES ( %(fname)s, %(lname)s, %(age)s, NOW(), NOW ());"
    #     return connectToMySQL("dojos_and_ninjas").query_db(query, data)