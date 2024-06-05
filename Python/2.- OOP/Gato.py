#from Archivo import Clase
from Animal import Animal

#class Hijo(Padre):
class Gato(Animal):

    #michi = Gato("Michi", "purrrr", "corto")
    #nombre = "Michi", sonido="purrr", tipo_pelaje="corto"
    #Animal("Michi", "purrr")
    def __init__(self, nombre, sonido, tipo_pelaje):
        super().__init__(nombre, sonido)
        self.tipo_pelaje = tipo_pelaje
    
    #rascarSofa
    def rascar_sofa(self):
        print(f"{self.nombre} está rascando el sofá de su casa")

    #Sobreescritura/Anulación
    def hacer_sonido(self):
        print(f"El gato te ve un momento, se aleja de ti y dice: {self.sonido}")
    
    def ir_al_bano(self):
        print("Va a su caja, razca la arena y va al baño")