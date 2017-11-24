'''1.	Escribir un programa que, dada una lista de palabras, genere una nueva
lista con las palabras que tienen una longitud  de 2 o más caracteres y que
además el primer y último caracter de las palabras sea igual.'''

listaPalabras = ['leal', 'Hola', 'Diego', 'ala', 'pared', 'cuadro', 'ocioso', 'feliz', 'amapola']
listaNueva = []
for palabra in listaPalabras:
    if len(palabra)>=2 and palabra[0]==palabra[-1]:
        listaNueva.append(palabra)
print("Lista generada:", listaNueva)

'''2.	Crear un programa que mantenga el rastro de los productos de una lista
de compras. El Programa debe estar preguntando por nuevos productos hasta que
el usuario no ingresa un valor “” (nada en el input, seguido de la tecla enter).
Al finalizar el programa debe presentar la lista de compras.
'''
compras = []
vacio=False
while not vacio:
    producto = input("Ingrese producto:")
    if not(producto=="" or len(producto)==0):
        compras.append(producto)
    else:
        vacio = True
print(compras)

'''3.	Implemente un programa que realice la misma operación que las siguientes funciones en Python. Imagine que no existen, ¿Cómo lo resolvería?
listaA = [1, 1, 2, 3, 5, 8, 5, 21, 34, 55, 89]
a)	count
b)	in
'''
listaA = [1, 1, 2, 3, 5, 8, 5, 21, 34, 55, 89]
buscar = 1
cont = 0
for i in range(len(listaA)):
    if listaA[i]==buscar:
        cont+=1
print("El número "+str(buscar)+" se encontró:", cont,"veces")

listaA = [1, 1, 2, 3, 5, 8, 5, 21, 34, 55, 89]
buscar = 20
resultado = False
for i in range(len(listaA)):
    if listaA[i]==buscar:
        resultado=True
print("El número "+str(buscar)+" fue encontrado:", resultado)

'''4.	Escriba un programa que dadas dos listas de numero genere una tercera
lista solo con los elementos que coinciden en ambas listas.
'''
listaA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listaB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listaC = []
for i in listaA:
    if i in listaB:
        listaC.append(i)
print("Nueva lista repetidos A en B:", listaC)