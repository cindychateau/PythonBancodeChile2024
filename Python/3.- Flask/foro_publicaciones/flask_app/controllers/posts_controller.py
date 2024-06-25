from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Modelos que vamos a utilizar
from flask_app.models.post import Post

@app.route("/create_post", methods=["POST"])
def create_post():
    #request.form = {"content": "contenido publ", "user_id": 1}
    if not Post.validate_post(request.form):
        return redirect("/dashboard")
    
    Post.save(request.form)
    return redirect("/dashboard")