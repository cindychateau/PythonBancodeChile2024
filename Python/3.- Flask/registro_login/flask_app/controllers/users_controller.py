from flask import Flask, render_template, redirect, request, session
from flask_app import app

#Importamos los modelos
from flask_app.models.user import User

#Importar BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Plantilla que muestra formularios
@app.route("/")
def index():
    return render_template("index.html")

#Ruta que recibe el formulario
@app.route("/register", methods=['POST'])
def register():
    #request.form = {"first_name": "Elena", "last_name": "De Troya"....}

    #Validar la info que recibimos
    if not User.validate_user(request.form):
        #No es valida la info, redirecciono al form
        return redirect("/")

    #Hashear contraseña
    pass_hash = bcrypt.generate_password_hash(request.form["password"])
    
    #Crear un diccionario que simule el form, incluyendo la contraseña hasheada
    form = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pass_hash
    }

    id = User.save(form) #Recibo el ID del nuevo usuario 1
    session["user_id"] = id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
