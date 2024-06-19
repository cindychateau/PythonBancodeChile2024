from flask import Flask, render_template, redirect, request

#Importo app
from flask_app import app

#Importo modelos
from flask_app.models.curso import Curso

@app.route("/")
def index():
    return redirect("/cursos")

@app.route("/cursos")
def cursos():
    lista_cursos = Curso.todos_cursos()
    return render_template("cursos.html", cursos = lista_cursos)


@app.route("/crear/curso")