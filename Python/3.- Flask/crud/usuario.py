from mysqlconnection import connectToMySQL
class Usuario:

    def __init__(self, data):
        '''
        data = {"id":1, "nombre": "Elena", "apellido": "De Troya", "email": "elena@cd.com", ...}
        '''
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    #Métodos que realicen las consultas
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"nombre": "Juana", "apellido": "De Arco"....}
        consulta = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s)"
        
        resultado = connectToMySQL('crud_bc').query_db(consulta, formulario)
        return resultado #el id del nuevo registro
    
    #Método que regrese todos los usuarios
    @classmethod
    def mostrar_usuarios(cls):
        query = "SELECT * FROM usuarios"
        resultado = connectToMySQL("crud_bc").query_db(query) #lista de diccionarios
        '''
        resultado = [
            {"id":1, "nombre": "Elena", "apellido": "De Troya", "email": "elena@cd.com", ...},
            {"id":2,"nombre": "Juana", "apellido": "De Arco"...}
        ]
        '''

        lista_usuarios = []
        for u in resultado:
            #u = {"id":1, "nombre": "Elena", "apellido": "De Troya", "email": "elena@cd.com", ...}
            usuario = cls(u) #Crea una instancia de usuario con los datos de un diccionario
            lista_usuarios.append(usuario) #Esa instancia la agrega a la lista
        
        return lista_usuarios #lista de instancias