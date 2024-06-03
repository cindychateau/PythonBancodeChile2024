#Importar la clase
from Persona import Persona

elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 18) #creando instancia de Persona
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 22)

print(elena.nombre)
print(juana.nombre)
elena.imprimir()

juana.saludar()
elena.saludar()

juana.codificar(15)

juana.codificar(100)
print(juana.lineas_codigo)