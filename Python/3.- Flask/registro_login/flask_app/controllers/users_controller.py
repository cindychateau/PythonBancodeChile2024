from flask import Flask, render_template, redirect, request, session
from flask_app import app

#Importamos los modelos
from flask_app.models.user import User

#PEND: Importar BCrypt

#Plantilla que muestra formularios
@app.route("/")
def index():
    return render_template("index.html")