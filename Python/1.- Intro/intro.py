#Para ejecutar en MAC: python3 nombre_archivo.py
#Para ejecutar en Windows: python nombre_archivo.py
print("Hola mundo!")

#Booleans
booleano = True #True o False

#Numerales
num = 10 #numero entero
fl = 10.99 #numero flotante / con punto decimal
#parseInt parseFloat
nuevo_float = float(num) #Forzando a mi número entero a que se convierta en flotante
print(nuevo_float)
nuevo_entero = int(fl) #Forzando a mi número con decimal a que se convierta en entero
print(nuevo_entero)
print(round(fl))

import random #Importando librería random
num_aleatorio = random.randint(1, 5) #Número aleatorio entre 1 y 5
print(num_aleatorio)

#Cadenas/Textos/Strings
abc = "ABCDEFG"
otro_texto = "Otro texto."
print("Este es el abecedario", abc) #La coma agregar un espacio entre los textos
print("Este es el abecedario "+abc) #el + concatena las cadenas tal cual son
print(otro_texto+" "+abc)
print(otro_texto,abc)
print("Este es un numero", num)
#print("Este es un numero"+ num) #ERROR:TypeError: can only concatenate str (not "int") to str
print("Este es un numero:" + str(num)) #Forzar un dato a que sea string

nombre = "Juana"
apodo = "juanita"
print(f"Hola, te presento a {nombre}, le puedes llamar '{apodo}' .") #Interpolación
print("Hola, te presento a "+nombre+", le puedes llamar '"+apodo+"' .")

#Métodos de manipulación de cadenas
frase = "hola mundo! soy Juana de Arco y hoy es 27 de Mayo"
print(frase.title()) #Primera letra de cada palabra esté en mayúscula
print(frase.upper()) #Todo esté en mayúsculas
print(frase.lower()) #Todo esté es minúsculas
print(frase.count('oy')) #Regresa cuántos 'oy' hay en la cadena
print(frase.find('Juana')) #Regresar el indice en el que encuentra mi palabra. Case-sensitive
print(frase.find('juana')) #-1 es que NO existe, o no encontró esa palabra en la frase
print(frase[-1]) #Regresa la última letra

#====Estructuras de Datos====
#TUPLAS: funciona parecido a un arreglo. NO puedo cambiar el valor
tupla = ("Elena", "Juana", "Pedro", "Pablo")
print(tupla[0]) #tupla[indice]
#tupla[1] = "Juanita" #ERROR TypeError: 'tuple' object does not support item assignment
tupla2 = ("texto", 7, False, 6.6) #Pueden tener distintos tipos de datos

#LISTAS / ARRAY / ARREGLO
lista_nombres = ["Hugo", "Paco", "Luis"]
print(lista_nombres[2])
lista_nombres[2] = "Donald"
print(lista_nombres)
lista_nombres.pop() #Elimina la última posición de mi lista
print(lista_nombres)
lista_nombres.pop(0) #Elimina el indice
print(lista_nombres)
lista_nombres.append("Mickey") #Se agrega el elemento al final de la lista
print(lista_nombres)
lista_nombres.insert(1, "Goofy") #Indico la posicion y el valor a agregar
print(lista_nombres)

lista_mix = ["texto", 11, True, 1.1, ["elemento1", "elemento2"]]
matriz = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9]
]
print(matriz[1][2])
print(lista_mix[4][1])

#DICCIONARIOS (Javascript Objetos)
estudiante = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "edad": 18,
    "soltera": True,
    "hobbies": ["leer", "comer", "salir al parque"]
}

print(estudiante["nombre"])
estudiante["edad"] = 19
print(estudiante)
estudiante["estatura"] = 1.67
print(estudiante)
estudiante.pop("soltera") #.pop(clave) : Elimina ese par de clave-valor
print(estudiante)

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", 
    "apellido": "Páramo", 
    "id": 345, 
    "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos MERN para Pedro?
#lista_alumnos[2]["cursos"].pop(2) #elimina el indice
lista_alumnos[2]["cursos"].remove("MERN") #elimina el valor
print(lista_alumnos)
'''
Comentarios
mas extensos
'''
from pprint import pprint #Importando la función pprint de la librería pprint
pprint(lista_alumnos)