cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario2(llave, lista): #funcion
    for dicc in lista:
        print(dicc[llave])

iterarDiccionario2("nombre", cantantes) #llamada a la funcion

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}
'''
diccionario = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}
clave = "ciudades"
diccionario[clave] = diccionario["ciudades"]
lista = ["San José", "Limón", "Cartago", "Puntarenas"]
'''
def imprimirInformacion(diccionario):
    for clave in diccionario: #recorro un diccionario, sus claves
        lista = diccionario[clave]
        print(len(lista), clave.upper())
        for elemento in lista:
            print(elemento)


imprimirInformacion(costa_rica)