#Importación de app
from flask_app import app

#Importación Controladores
from flask_app.controllers import curso_controller, estudiante_controller

#Ejecución de app
if __name__=="__main__":
	app.run(debug=True)