from flask_app.config.mysqlconnection import connectToMySQL #Importacion de la conexión con sql

from flask import flash #flash es el encargado de mostrar los mensajes

from datetime import datetime #Manipular las fechas

class Event:

    def __init__(self, data):
        #data = {diccionario con la info de la base de datos}
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.date = data["date"]
        self.details = data["details"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"] #Columna extra al hacer una consulta JOIN
    
    @classmethod
    def create(cls, form):
        #form = {"name": "Examen de Python", "location": "Casa", "date": "2024-06-28".... "user_id": 1}
        query = "INSERT INTO events (name, location, date, details, user_id) VALUES (%(name)s, %(location)s, %(date)s, %(details)s, %(user_id)s) "
        return connectToMySQL("events_bc").query_db(query, form)
    
    #CRUD: Create Read Update Delete

    @classmethod
    def read_one(cls, data):
        #data = {"id": 1}
        query = "SELECT events.*, users.first_name as user_name FROM events JOIN users ON events.user_id = users.id WHERE events.id = %(id)s;" 
        #Lista con 1 diccionario
        result = connectToMySQL("events_bc").query_db(query, data) #Lista de Diccionarios
        #result = [ {"id": 1, "name": "Examen", "location": "Casa", "date": 2024-06-28....} ]
        event = cls(result[0]) #Objeto Event
        return event

    @classmethod
    def read_all(cls):
        #WHERE date >= CURDATE() -> Solo eventos de hoy y del futuro
        #ORDER BY date ASC -> Ordena los eventos de maner asc
        query = "SELECT events.*, users.first_name as user_name FROM events JOIN users ON events.user_id = users.id WHERE date >= CURDATE() ORDER BY date ASC;"
        results = connectToMySQL("events_bc").query_db(query) #Lista de Diccionarios
        events = []
        for ev in results:
            events.append(cls(ev)) #ev = {diccionario con la info de bd}, cls(ev): Crear el objeto Event, events.append(): el objeto Event lo agrego a la lista
        return events
    
    @staticmethod
    def validate_event(form):
        #form = {"name": "Examen de Python", "location": "Casa", "date": "2024-06-28".... "user_id": 1}
        is_valid = True

        if len(form["name"]) < 3:
            flash("El nombre del evento debe tener al menos 3 caracteres", "evento") #(mensaje, categoria)
            is_valid = False
        
        #Validar que el nombre del evento sea único
        else:
            query=""
            if "id" not in form:
                query = "SELECT * FROM events WHERE name = %(name)s AND id != 0"
            else:
                query = "SELECT * FROM events WHERE name = %(name)s AND id != %(id)s"
            result = connectToMySQL("events_bc").query_db(query, form) #Lista de eventos
            #Lista vacía, Lista con 1 diccionario
            if len(result) >= 1:
                #SI existe ese nombre de evento en mi BD
                flash(f"Un evento con el nombre '{form["name"]}' ya fué creado", "evento")
                is_valid = False

        if len(form["location"]) < 3:
            flash("La ubicación del evento debe tener al menos 3 caracteres", "evento") #(mensaje, categoria)
            is_valid = False 

        if len(form["details"]) < 3:
            flash("Los detalles del evento deben tener al menos 3 caracteres", "evento") #(mensaje, categoria)
            is_valid = False   

        if form["date"] == "":
            flash("Ingrese una fecha", "evento")
            is_valid = False
        else:
            #Validar que la fecha sea en el futuro
            fecha_obj = datetime.strptime(form["date"], '%Y-%m-%d') #Creando una fecha en base al string que recibo del form
            hoy = datetime.now()
            if hoy > fecha_obj:
                flash('La fecha no puede ser en el pasado', 'evento')
                is_valid = False

        return is_valid #True o False

    #update
    @classmethod
    def update(cls, form):
        #form = {la informacion que se envió en el formulario}
        query = "UPDATE events SET name=%(name)s, location=%(location)s, date=%(date)s, details=%(details)s, user_id=%(user_id)s WHERE id=%(id)s"
        return connectToMySQL("events_bc").query_db(query, form)

    #delete
    @classmethod
    def delete(cls, data):
        #data = {"id": 1}
        query = "DELETE FROM events WHERE id = %(id)s"
        return connectToMySQL("events_bc").query_db(query, data)
