class Persona:

    #Método constructor: se encarga de inicializar el objeto
    '''
    self = juana
    nombre = "Juana"
    apellido = "De Arco"
    email = "juana@codingdojo.com"
    edad = 22
    '''
    def __init__(self, nombre, apellido, email, edad):
        # Codigo
        self.nombre = nombre #juana.nombre = "Juana"
        self.apellido = apellido #juana.apellido = "De Arco"
        self.email = email #juana.email = "juana@codingdojo.com"
        self.lineas_codigo = 0 #lineas de codigo que ha desarrollado
        self.edad = edad #juana.edad = 22
    
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