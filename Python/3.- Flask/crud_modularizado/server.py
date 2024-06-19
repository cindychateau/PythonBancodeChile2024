#python3 o python -m pipenv install flask pymysql
#pipenv install flask pymysql ->Instalar y generar los Pipfiles (OJO solo es necesaria 1 vez)
#pipenv shell -> Activa entorno virtual
#python3 server.py -> Ejecuta mi app

#Ctrl + C -> Detener app
#exit -> Salir del entorno virtual

#Importación de flask_app
from flask_app import app

#Importación controladores
from flask_app.controllers import usuarios_controller

#Ejecución de la app
if __name__ == "__main__":
    app.run(debug=True)