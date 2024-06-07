from flask import Flask, render_template

app = Flask(__name__)

#RUTAS
@app.route("/loteria")
def nivel1():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)