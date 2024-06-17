from mysqlconnection import connectToMySQL
class Usuario:

    def __init__(self, data):
        '''
        data = {
            "id": 1,
            "nombre": "Elena",
            "apellido": "De Troya",
            "email": "elena@cd.com"
        }
        '''
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    #Métodos que realicen las consultas
