'''
Activamos entorno virtual --> pipenv shell
Despliegue servidor ---> python server.py o python3 server.py
ctrl + c ---> Para detener el servidor 
exit ---> Para salirnos del entorno virtual
'''
from flask import Flask, render_template #Importa Flask y me permite crear la aplicación web

app = Flask(__name__) #Crea una nueva instancia de la clase Flask llamada "app"

@app.route("/") #Decorado @, genera la ruta "/" (raíz) y asociamos con la función inmediata
def inicio():
    return "¡Hola desde Flask! :)" #Devolver el texto "¡Hola desde Flask!"

@app.route("/hola/<name>") #/hola/Elena  name="Elena"
def hola(name):
    return "Hola "+name

@app.route("/numero/<int:n>") #Forzosamente indico que en ese espacio debe ir un entero
def numero(n):
    print(f"El usuario ingresó {n}")
    respuesta = f"<h1>Ingresaste el numero {n}</h1>"
    return respuesta

@app.route("/bienvenidas")
def bienvenidas():
    return render_template("index.html")

# /usuarios/Pedro Paramo/5
@app.route("/usuarios/<name>/<int:num>")
def usuarios(name, num):
    #name = "Pedro Paramo"
    #num = 5
    usuarios = ["Juana de Arco", "Pablo Picasso", "Pedro Páramo"]
    return render_template("usuarios.html", nombre=name, numero=num, usuarios=usuarios)

#Asegura que este archivo que el se está ejecutando directamente en el módulo
if __name__ == "__main__": 
    app.run(debug=True) #Ejecuta mi aplicación, en modo depuración