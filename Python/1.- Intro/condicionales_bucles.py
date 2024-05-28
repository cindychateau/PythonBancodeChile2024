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