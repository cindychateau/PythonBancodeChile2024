from Animal import Animal

class Perro(Animal):

    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza = raza
    
    def perseguir_autos(self):
        print(f"{self.nombre} está persiguiendo un auto!")
    
    def ir_al_bano(self):
        print("Sale a pasear, va al baño y su dueño recoge todo con una bolsita")