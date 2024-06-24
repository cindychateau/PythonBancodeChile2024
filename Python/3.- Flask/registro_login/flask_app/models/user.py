from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        #data = {diccionario con toda la info del objeto}
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    #Método que crea un nuevo registro - Registro
    @classmethod
    def save(cls, form):
        #form = {"first_name": "Elena", "last_name": "De Troya", "email": "elena@cd.com", "password": "YA ESTE HASHEADO"}
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s) "
        return connectToMySQL("loginreg_bc").query_db(query, form) #Regresar el ID del nuevo registro
    
    #Método que regresa objeto de Usuario en base a e-mail - Inicio de Sesión
    @classmethod
    def get_by_email(cls, form): #cls = User
        #form = {"email": "elena@cd.com", "password": "hola123"}
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL("loginreg_bc").query_db(query, form) #Regresa Lista de Diccionarios
        
        if len(result) < 1: #Revisa que mi lista esté vacía
            return False
        else:
            #Me regresa 1 registro
            #result = [ {"id": 1, "first_name": "Elena", "last_name": "De Troya".....} ]
            user = cls(result[0]) #User({"id": 1, "first_name": "Elena", "last_name": "De Troya".....})
            return user
