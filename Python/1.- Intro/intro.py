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
