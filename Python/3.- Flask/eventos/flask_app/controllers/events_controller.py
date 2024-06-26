from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Modelos
from flask_app.models.event import Event
from flask_app.models.user import User

@app.route("/nuevo")
def nuevo():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    #Va a recibir el formulario... request.form = diccionario con toda la info del formulario
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    if not Event.validate_event(request.form):
        return redirect("/nuevo")
    
    Event.create(request.form)
    return redirect("/dashboard")
