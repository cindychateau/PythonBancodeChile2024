class Animal:

    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        self.vacunas = False
    
    def hacer_sonido(self):
        print(f"El animalito {self.nombre} dice: {self.sonido}")

    def ponerle_vacuna(self):
        print(f"Vacunaste a {self.nombre}")
        self.vacunas = True