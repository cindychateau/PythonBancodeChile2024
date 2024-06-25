from flask import Flask #importación de flask

app = Flask(__name__) #Inicializamos la app

app.secret_key = "Llave secreta ;)" #Necesaria para la sesión