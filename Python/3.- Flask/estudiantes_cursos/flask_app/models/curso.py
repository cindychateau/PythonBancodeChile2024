from flask_app.config.mysqlconnection import connectToMySQL

#PEND: Importar tambien Estudiante

class Curso:

    def __init__(self, data):
        #data diccionario que tiene toda la información para el objeto
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        #Lo llenamos en una función
        self.estudiantes = []
    
    @classmethod
    def todos_cursos(cls):
        query = "SELECT * FROM cursos"
        resultados = connectToMySQL('esquema_estudiantes_cursos').query_db(query) #Lista de diccionarios
        cursos = []

        for curso in resultados:
            cursos.append(cls(curso)) #1.- cls(curso) crea el objeto. 2.- el objeto se ingresa en la lista cursos
        return cursos
    
    @classmethod
    def guardar(cls, formulario):
        #formulario = {"nombre": "MERN"}
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s) "
        resultado = connectToMySQL('esquema_estudiantes_cursos').query_db(query, formulario)
        return resultado

    #Método que me regrese UN curso con sus estudiantes
