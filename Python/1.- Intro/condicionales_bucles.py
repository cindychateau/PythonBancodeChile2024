#Para ejecutar MAC: python3 nombre_archivo.py
#Para ejecutar Windows: python nombre_archivo.py .... py nombre_archivo.py

#==== CONDICIONALES ====
x = 20
if x > 10:
    print("El numero ingresado es mayor a 10")
    print("El numero es:", x)
    print(f"El numero es: {x}. Es decir, el numero es: {x} ") #Format: interpolar variables
    #Otra
    #Otra
else:
    print("El numero es menor o igual a 10")

edad_infante = 4
if edad_infante < 2:
    print("Es un bebe")
elif edad_infante < 5: #elif = else if
    print("Es un toddler")
else:
    print("Es un niño")

y = 5
if y > 3:
    print("Numero mayor a 3")
else:
    print("Numero menor o igual a 3")
    print("tu numero es menor a 3")

temperatura = 20
estaLloviendo = False
if temperatura > 18 and not estaLloviendo: #and == && not = !
    print("Salgamos a pasear al parque")

edad = input("Ingresa tu edad:") #str
edad = int(edad)
permisoPadres = True
if edad > 18 or permisoPadres: #si una u otra se cumple
    print("Puedes obtener tu licencia de manejo")
    #Otra linea
    #Otra linea
    #Otra linea

#==== BUCLE/CICLOS ====
for x in range(5): #Rango 0-4. 5 YA NO ENTRA. x < 5
    print(x)

print("-------")

for y in range(5, 13): #(Comienzo, Fin) -> y=5; y<13
    print(y)

print("-------")

for z in range(2, 12, 2): #(Comienzo, Fin, Paso) -> z=2; z < 12; z+=2
    print(z)

print("-------")

for m in range(30, 15, -2):
    print(m)

#RECORRER UN ARREGLO
lista_nombres = ["Elena", "Juana", "Pablo", "Pedro"]
for nombre in lista_nombres:
    print(nombre)

for indice in range(len(lista_nombres)): #i=0; i < 4. i = indice
    print(f"Indice: {indice}; Valor: {lista_nombres[indice]}")

estudiante = { #Equivalente a objetos en javascript
    "nombre": "Elena", #clave: valor
    "apellido": "De Troya",
    "edad": 19
}
'''
dato = "nombre"
print Clave:nombre. Valor: Elena
---
dato = "apellido"
print Clave: apellido. Valor: De Troya
---
dato = "edad"
print Clave: edad. Valor: 19
'''
for dato in estudiante: #recorre claves
    print(f"Clave: {dato}. Valor:{estudiante[dato]}")

lista_estudiantes = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345}
]

for estudiante in lista_estudiantes:
    print(estudiante)
    for dato in estudiante:
        print(f"Clave: {dato}. Valor:{estudiante[dato]}")
