# CRUD: Create Read Update Delete = Crear Leer Actualizar Borrar
# pipenv install flask pymysql
from flask import Flask, render_template, request, redirect

from usuario import Usuario

app = Flask(__name__)

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

if __name__=="__main__":
    app.run(debug=True)