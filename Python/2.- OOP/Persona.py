from Animal import Animal
class Persona:

    #Atributo de Clase: es un atributo que pertenece a la clase completa y que el valor es compartido por todas las instancias
    escuela = "Coding Dojo LATAM"
    lista_personas = []

    #Método constructor: se encarga de inicializar el objeto
    '''
    self = juana
    nombre = "Juana"
    apellido = "De Arco"
    email = "juana@codingdojo.com"
    edad = 22
    '''
    def __init__(self, name, last_name, e_mail, age, nombre_mascota, sonido_mascota):
        # Codigo
        self.nombre = name #juana.nombre = "Juana"
        self.apellido = last_name #juana.apellido = "De Arco"
        self.email = e_mail #juana.email = "juana@codingdojo.com"
        self.lineas_codigo = 0 #lineas de codigo que ha desarrollado
        self.edad = age #juana.edad = 22
        #self.mascota = animalito #juana.mascota = firulais
        self.mascota = Animal(nombre_mascota, sonido_mascota)


        # Cada nueva instancia se agrega a la lista de personas
        #lista_personas = [elena, juana]
        Persona.lista_personas.append(self)
    
    #self = elena
    def imprimir(self):
        print(self.nombre, self.apellido, self.email)
    
    #self es el objeto que invoca a la función
    #self = elena
    def saludar(self):
        print(f"Te saluda {self.nombre}. ¡Holiiii!")

    #self = juana
    #cantidad_lineas = 100
    #juana.lineas_codigo = 15 + 100 = 115
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
    
    #método de clase
    #cls se refiere a la clase que invoca al  métodos
    '''
    Persona.lista_personas = [elena, juana, pedro]
    cls = Persona
    p = elena
    Elena De Troya 18
    ---
    p = juana
    Juana De Arco 22
    ---
    p = pedro
    Pedro Paramo 32
    '''
    @classmethod
    def imprimir_todos(cls): 
        #cls = Persona
        for p in cls.lista_personas:
            p.imprimir()
    

    #Métodos estáticos: ayudantes/auxiliares
    @staticmethod
    def mayor_edad(edad):
        #edad = 22
        if edad < 18:
            return False
        else:
            return True
    


    def licencia_conducir(self):
        #mayor_edad(22)
        if(Persona.mayor_edad(self.edad)):
            print("Puedes obtener tu licencia")
        else:
            print("No tienes la mayoria de edad")
    
    def pasear_mascota(self):
        print("Estas paseando a tu mascota, y como se puso feliz hizo un sonido")
        self.mascota.hacer_sonido()

