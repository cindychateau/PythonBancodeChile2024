from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) #Creando Instancia

app.secret_key = "llave secreta!"

@app.route("/")
def index():
    #la primera vez que entro
    if "contador" not in session:
        #No existe en sesión contador
        session["contador"] = 0
    else:
        #SI existe
        session["contador"] += 1

    return render_template("index.html")

@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")

@app.route("/visitar_2")
def visitar_2():
    session["contador"] += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)