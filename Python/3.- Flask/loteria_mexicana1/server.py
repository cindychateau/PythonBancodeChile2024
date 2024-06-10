import math
import random
from flask import Flask, render_template

app = Flask(__name__)


cartas = ["1  El Gallo",

          "2  El Diablito",

          "3  La Dama",

          "4  El catrín",

          "5  El paraguas",

          "6  La sirena",

          "7  La escalera",

          "8  La botella",

          "9  El barril",

          "10 El árbol",

          "11 El melón",

          "12 El valiente",

          "13 El gorrito",

          "14 La muerte",

          "15 La pera",

          "16 La bandera",

          "17 El bandolón",

          "18 El violoncello",

          "19 La garza",

          "20 El pájaro",

          "21 La mano",

          "22 La bota",

          "23 La luna",

          "24 El cotorro",

          "25 El borracho",

          "26 El negrito",

          "27 El corazón",

          "28 La sandía",

          "29 El tambor",

          "30 El camarón",

          "31 Las jaras",

          "32 El músico",

          "33 La araña",

          "34 El soldado",

          "35 La estrella",

          "36 El cazo",

          "37 El mundo",

          "38 El apache",

          "39 El nopal",

          "40 El alacrán",

          "41 La rosa",

          "42 La calavera",

          "43 La campana",

          "44 El cantarito",

          "45 El venado",

          "46 El sol",

          "47 La corona",

          "48 La chalupa",

          "49 El pino",

          "50 El pescado",

          "51 La palma",

          "52 La maceta",

          "53 El arpa",

          "54 La rana"]

# RUTAS


@app.route("/loteria")
def nivel1():

    aleatorias = random.sample(cartas, 4*4)
    return render_template("index.html", filas=4, columnas=4, cartas=aleatorias)

# @app.route("/loteria/<int:filas>")
# def nivel2(filas):
#     print(filas)
#     colores=["rosa","azul","amarillo"]
#     return render_template("loteria4xn.html", filas=filas,colores=colores)


@app.route("/loteria/<int:filas>")  # /loteria/10
def nivel2(filas):  # filas = 10
    # enviando filas=10
    # PERMITE SABER CUANTOS SETS DE CARTAS SE NECESITAN
    repeticiones = math.ceil((filas*4)/len(cartas))
    # crea un arreglo con las repeticiones necesarias por cartas
    counts = [repeticiones] * len(cartas)
    aleatorias = random.sample(cartas, filas*4, counts=counts)
    return render_template("index.html", filas=filas, columnas=4, cartas=aleatorias)


@app.route("/loteria/<int:filas>/<int:columnas>")
def nivel3(filas, columnas):

    # PERMITE SABER CUANTOS SETS DE CARTAS SE NECESITAN
    repeticiones = math.ceil((filas*columnas)/len(cartas))
    # crea un arreglo con las repeticiones necesarias por cartas
    counts = [repeticiones] * len(cartas)

    aleatorias = random.sample(
        population=cartas, k=filas*columnas, counts=counts)
    print(aleatorias)
    return render_template("index.html", filas=filas, columnas=columnas, cartas=aleatorias)


if __name__ == "__main__":
    app.run(debug=True)
