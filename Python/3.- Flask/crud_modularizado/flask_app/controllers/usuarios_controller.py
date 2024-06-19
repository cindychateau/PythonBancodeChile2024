#Importaciones
from flask import Flask, render_template, request, redirect, session

#Importar la app
from flask_app import app

#Importar los modelos a utilizar
from flask_app.models.usuario import Usuario

#RUTAS
@app.route("/")
def index():
    #enviar todos los usuarios
    usuarios = Usuario.mostrar_usuarios() #lista con todos los usuarios
    return render_template("index.html", listado_usuarios = usuarios)

@app.route("/nuevo")
def nuevo():
    return render_template("nuevo.html")

@app.route("/crear", methods=["POST"])
def crear():
    #Recibimos lo que el usuario ingreso en form
    #request.form = DICCIONARIO con la info
    Usuario.guardar(request.form)
    return redirect("/")

@app.route("/borrar/<int:id>") #/borrar/2
def borrar(id): #id = 2
    diccionario = {"id": id} #{"id": 2}
    Usuario.eliminar(diccionario)
    return redirect("/")

@app.route("/editar/<int:id>") #/editar/2
def editar(id):
    #Una función en Usuario que en base a un ID me regrese una instancia de Usuario
    diccionario = {"id": id} #{"id": 2}
    usuario = Usuario.mostrar_un_usuario(diccionario)
    return render_template("editar.html", usuario=usuario) #enviando el objeto de Usuario a editar

@app.route("/actualizar", methods=['POST'])
def actualizar():
    #recibimos el request.form
    #Un método en Usuario que actulice la info de un registro enviando request.form
    Usuario.actualizar_usuario(request.form)
    return redirect("/")