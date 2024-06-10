#Importamos Flask (encargado de crear la aplicación)
#render_template (renderizar los HTML)
#request (con el cual nosotros podemos recibir información de formularios)
#redirect (redireccionar)
from flask import Flask, render_template, request, redirect

app = Flask(__name__) #Instancia de Flask = Aplicación Web

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
    #Renderizar = Mostrar una plantilla HTML
    #NUNCA renderizamos una plantilla cuando recibo un POST
    #En su lugar: redirigimos a otra ruta /exito
    return redirect("/exito")

#3.- Ruta a la que redirigimos
@app.route("/exito")
def exito():
    return render_template("exito.html")
    


if __name__ == "__main__":
    app.run(debug=True)