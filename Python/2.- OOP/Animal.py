class Animal:

    #name="Michi", sound = "purrr"
    #michi.nombre = "Michi"
    #michi.sonido = "purrr"
    def __init__(self, name, sound):
        self.nombre = name
        self.sonido = sound
        self.vacunas = False #Valor por defecto
    
    def hacer_sonido(self):
        print(f"El animalito {self.nombre} dice: {self.sonido}")

    def ponerle_vacuna(self):
        print(f"Vacunaste a {self.nombre}")
        self.vacunas = True
    
    #Método "en blanco" que debe implementarse en las clases hijas
    def ir_al_bano(self):
        raise NotImplementedError