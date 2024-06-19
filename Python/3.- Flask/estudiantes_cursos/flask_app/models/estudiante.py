from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:

    def __init__(self, data):
        #data es el diccionario con toda la info del estudiante
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.curso_id = data["curso_id"]
    
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"nombre": "Elena", "apellido": "De Troya", "edad": 15, "curso_id": 1}
        query = "INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s) "
        return connectToMySQL("esquema_estudiantes_cursos").query_db(query, formulario)
    
