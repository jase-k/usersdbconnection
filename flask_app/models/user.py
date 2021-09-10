from flask_app.config.mysqlconnection import MySQLConnection

class User:
    def __init__(self, data):
        self.fname = data['first_name'], 
        self.lname = data['last_name'], 
        self.email = data['email'],
        self.created = data['created_at'],
        self.updated = data['updated_at']
    
    @classmethod
    def addUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) Values( %(fname)s, %(lname)s, %(email)s, NOW(), NOW() )"
        results = MySQLConnection('users_schema').query_db(query, data)
        return results
    
    @classmethod
    def getUsers(cls):
        query = "Select * from users"

        results = MySQLConnection('users_schema').query_db(query)
        
        return results
    @classmethod
    def getUserById(cls, id):
        data = {
            "id" : id
        }
        query = "Select * from users WHERE id = %(id)s"

        results = MySQLConnection('users_schema').query_db(query, data)

        return results
    
    @classmethod
    def updateUser(cls, data):
        query = "Update users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"

        MySQLConnection('users_schema').query_db(query, data)
    
    @classmethod
    def deleteUser(cls, id):
        query = f"DELETE from users WHERE id = {id}"
        
        MySQLConnection('users_schema').query_db(query)