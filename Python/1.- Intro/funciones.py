#Función: Un bloque de código dedicado a una tarea específica que puede invocarse/llamarse las veces que necesitemos. 

#def: define -> Definiendo una función
def saludo():
    print("¡Hola mundo!")

#nombre = "Juana"
def saludoNombre(nombre):
    print(f"¡Hola {nombre}!")

'''
lista = ["Elena", "Juana", "Pedro"]
nombre = "Elena"
¡Hola Elena!
--
nombre = "Juana"
¡Hola Juana!
--
nombre = "Pedro"
¡Hola Pedro!
'''
def saludoLista(lista):
    for nombre in lista:
        print(f"¡Hola {nombre}!")   

saludo()
saludo()
saludoNombre("Elena")
saludoNombre("Juana")
saludoLista(["Elena", "Juana", "Pedro"])

#num1 = 5; num2 = 6
def sumatoria(num1, num2):
    print(num1+num2) #5+6 print 11

#num1 = 7; num2 = 7
def sumatoriaReturn(num1, num2):
    sumatoria(num1, num2)
    return num1+num2 #14

sumatoria(5, 6)
#resultado = 11 + 14 =  25
resultado = sumatoriaReturn(5, 6) + sumatoriaReturn(7, 7)
print(resultado)

#apellido = "De Arco"
def hello(nombre="Elena", apellido="De Troya"):
    print(f"¡Hola {nombre} {apellido}!")

hello()
hello("Juana") #Si no especifico qué parámetro es, lo relevante es el orden
hello(apellido="De Arco") #Al especificar el parámetro, ese sería el valor de la variable
hello(apellido="De Arco", nombre="Juana")
hello("Juana", "De Arco")

#num1 = 4; num2 = 5
def multiplicacion(num1=1, num2=1):
    return num1*num2 #4*5 <- 20

resultado_multiplicacion = multiplicacion()
print( resultado_multiplicacion ) #1
print( multiplicacion(4) ) #4
print( multiplicacion(4, 5) ) #20
print( multiplicacion(4, "Hola") )