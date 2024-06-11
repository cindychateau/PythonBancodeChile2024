#Importamos Flask (encargado de crear la aplicación)
#render_template (renderizar los HTML)
#request (con el cual nosotros podemos recibir información de formularios)
#redirect (redireccionar)
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) #Instancia de Flask = Aplicación Web

app.secret_key = "llave super secreta" #una capa extra de seguridad para las cookies

#Formulario necesita 3 rutas:
#1.- Renderiza/Muestra el formulario
@app.route("/")
def index():
    return render_template("index.html")

#2.- Recibe la info del formulario
@app.route("/registrar", methods=['POST'])
def registrar():
    print(request.form)
    print(request.form['email'])
    '''
    request.form = {
        "nombre": "Juana de Arco",
        "email": "juana@codingdojo.com"
    }
    '''
    #Guardar en sesión
    session["usuario"] = request.form["nombre"]
    session["correo"] = request.form["email"]

    #Renderizar = Mostrar una plantilla HTML
    #NUNCA renderizamos una plantilla cuando recibo un POST
    #En su lugar: redirigimos a otra ruta /exito
    return redirect("/exito")

#3.- Ruta a la que redirigimos
@app.route("/exito")
def exito():
    #reviso que en sesión exista algo llamado usuario
    if "usuario" not in session:
        return redirect("/")
    
    return render_template("exito.html")

@app.route("/logout")
def logout():
    #Eliminar sesión
    session.clear()
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)