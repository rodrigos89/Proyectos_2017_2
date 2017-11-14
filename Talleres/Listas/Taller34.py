'''1.	Escribir un programa que, dada una lista de palabras,
genere una nueva lista con las palabras que contienen un
carácter ingresado por el usuario. Por ejemplo, si ingresa
la letra “a” o la letra “e”, se deben seleccionar solo las
palabras con las letras a, e:'''

listaPalabras = ['leal', 'Hola', 'Diego', 'ala', 'pared', 'cuadro', 'ocioso', 'feliz', 'amapola']
listaNueva = []
for palabra in listaPalabras:
    if "a" in palabra or "e" in palabra:
        listaNueva.append(palabra)
print("Lista generada:", listaNueva)

'''2.	Crear un programa que permite simular el juego de pozo millonario,
el usuario irá ingresando 15 números del 1 al 25 y los almacenará en una lista.
El Programa debe estar preguntando por nuevos números hasta que por error
ingresa un número fuera de ese rango. Es allí cundo su programa finaliza y
se imprimen los números que han salido hasta el momento.'''
pozo = []
cont=0
while cont<15:
    nro = input("Ingrese número:")
    if 0<int(nro)<=25:
        pozo.append(nro)
        cont+=1
    else:
        cont=15
print(pozo)

'''3.	Implemente un programa que realice la misma operación que las siguientes funciones en Python.
listaA = [1, 1, 2, 3, 5, 8, 5, 21, 34, 55, 89]
a)	index(var)
b)	replace(actual,nuevo)'''

listaA = [1, 1, 2, 3, 5, 8, 5, 21, 34, 55, 89]
buscar = 8
indice = -1
for i in range(len(listaA)):
    if listaA[i]==buscar:
        indice = i
        break
print("El índice de "+str(buscar)+" es:", indice)


valorRemplazar= 20
buscar=21
for i in range(len(listaA)):
    if listaA[i]==buscar:
        listaA[i]=valorRemplazar
        break
print("Luego de reemplazar "+str(buscar)+" por "+str(valorRemplazar)+" la lista actual es:", listaA)


'''4.	Escriba un programa que dadas dos listas de numero
genere una tercera lista solo con los elementos que no coinciden de A en B.'''

listaA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listaB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listaC = []
for ele in listaA:
    if ele not in listaB:
        listaC.append(ele)
print("Los elementos que no se repiten de A en B son:", listaC)