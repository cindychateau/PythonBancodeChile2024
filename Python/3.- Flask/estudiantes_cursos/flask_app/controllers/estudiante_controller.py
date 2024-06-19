from flask import Flask, render_template, redirect, request

from flask_app import app

from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso

@app.route("/estudiante")
def estudiante():
    lista_cursos = Curso.todos_cursos()
    return render_template("estudiante.html", cursos = lista_cursos)

@app.route("/crear/estudiante", methods=["POST"])
def crear_estudiante():
    Estudiante.guardar(request.form)
    return redirect("/cursos")