from flask import Flask, render_template

app = Flask(__name__)

# RUTAS


@app.route("/loteria")
def nivel1():
    return render_template("index.html")


@app.route("/loteria/<int:filas>")
def nivel2(filas):
    print(filas)
    colores=["rosa","azul","amarillo"]
    return render_template("loteria4xn.html", filas=filas,colores=colores)


if __name__ == "__main__":
    app.run(debug=True)
