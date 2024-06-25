from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #flash es el encargado de mostrar los mensajes

class Post:

    def __init__(self, data):
        #data = {diccionario con la info de mi bd}
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"]
    
    @classmethod
    def save(cls, form):
        #form = {"content": "contenido de la publicación", "user_id": 1}
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s) "
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def validate_post(form):
        #form = {"content": "contenido de la publicación", "user_id": 1}
        is_valid = True
        
        if len(form["content"]) < 1:
            flash("Post content is required.", "post") #(mensaje, categoria)
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT posts.*, users.first_name as user_name FROM posts JOIN users ON posts.user_id = users.id ORDER BY created_at DESC;"
        results = connectToMySQL("foro_publicaciones").query_db(query) #results = Lista de diccionarios
        posts = []
        for p in results:
            #p = {"id": 1, "content": "Hola"....., "user_name": "Elena"}
            posts.append(cls(p)) #1.- cls(post): Genera el objeto de publicacion con el diccionario. 2.- .append agrega el objeto a la lista de posts
        return posts
    
    @classmethod
    def delete(cls, data): #(cls, post_id)
        #data = {"id": 2} -> data = {"id": post_id}
        query = "DELETE FROM posts WHERE id = %(id)s"
        connectToMySQL("foro_publicaciones").query_db(query, data)