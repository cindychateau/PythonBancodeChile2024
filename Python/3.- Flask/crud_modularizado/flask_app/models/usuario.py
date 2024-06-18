from flask_app.config.mysqlconnection import connectToMySQL
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
    
    @classmethod
    def eliminar(cls, data): 
        #data = {"id": 1}
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        return connectToMySQL('crud_bc').query_db(query, data)
    
    @classmethod
    def mostrar_un_usuario(cls, data):
        #data = {"id": 1}
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultado = connectToMySQL('crud_bc').query_db(query, data) #Select me regresa una lista de diccionarios
        #resultado = [ {"id": 1, "nombre": "Elena", "apellido": "De Troya"....} ]
        usuario = cls(resultado[0]) #creo un objeto, con la info de la BD
        return usuario #instancia de Usuario
    
    @classmethod
    def actualizar_usuario(cls, formulario):
        '''
        formulario= {
            "id": 1
            "nombre": "elenita",
            "apellido":"de troya",
            "email": "elenita@cd.com"
        }
        '''
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s WHERE id = %(id)s"
        return connectToMySQL('crud_bc').query_db(query, formulario)
