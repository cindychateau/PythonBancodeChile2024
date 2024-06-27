from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Objetos: user.id
#Diccionarios: session["user_id"]
#Lista: result[0]

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

@app.route("/ver/<int:id>") #/ver/1
def read(id): #id = 1
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {"id": id} #{"id": 1}
    event = Event.read_one(dicc) #Invoco de la clase Event a read_one, enviamos el diccionario y recibimos un objeto Events

    return render_template("view.html", event=event)

@app.route("/borrar/<int:id>") #/borrar/2
def eliminar(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {"id": id} #{"id": 1}
    Event.delete(dicc)
    return redirect("/dashboard")

@app.route("/editar/<int:id>") #/editar/3
def edit(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")

    dicc = {"id": id} #{"id": 1}
    event = Event.read_one(dicc) #Invoco de la clase Event a read_one, enviamos el diccionario y recibimos un objeto Events

    #PEND: revisar que si sea el usuario en sesión el que creó el evento
    
    return render_template("edit.html", event=event)

@app.route("/update", methods=["POST"])
def update():
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Recibir request.form = diccionario con la informacion del formulario

    #Validamos
    if not Event.validate_event(request.form):
        return redirect("/editar/"+request.form["id"])

    Event.update(request.form)
    return redirect("/dashboard")