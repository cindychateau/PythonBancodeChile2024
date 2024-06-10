from flask import Flask, render_template

app = Flask(__name__)

# RUTAS


@app.route("/loteria")
def nivel1():
    return render_template("index.html", filas=4, columnas=4)

# @app.route("/loteria/<int:filas>")
# def nivel2(filas):
#     print(filas)
#     colores=["rosa","azul","amarillo"]
#     return render_template("loteria4xn.html", filas=filas,colores=colores)

@app.route("/loteria/<int:filas>") #/loteria/10
def nivel2(filas): #filas = 10
    return render_template("index.html", filas=filas, columnas=4) #enviando filas=10

@app.route("/loteria/<int:filas>/<int:columnas>")
def nivel3(filas, columnas):
    return render_template("index.html", filas=filas, columnas=columnas)

if __name__ == "__main__":
    app.run(debug=True)
