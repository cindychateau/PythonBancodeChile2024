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

print(juana.escuela)
print(elena.escuela)

#Cambiando para toda la clase la escuela
Persona.escuela = "Escuela de Programación"
print(juana.escuela)
print(elena.escuela)

pedro = Persona("Pedro", "Paramo", "pedro@codingdojo.com", 32)

print(len(Persona.lista_personas))

Persona.imprimir_todos()

pedro.licencia_conducir()