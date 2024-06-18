#Importar flask
from flask import Flask

#Inicializar la app
app = Flask(__name__)

#Declarar la llave secreta
app.secret_key = "llave secretisima"