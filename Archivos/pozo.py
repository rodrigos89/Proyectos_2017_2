import random as rd

def crearTabla(nombre):
    archivo = open(nombre+".txt", "w")
    lista = []
    while len(lista)<10:
        nro = str(rd.randint(1,20))
        if nro not in lista:
            lista.append(nro)
    nros = ",".join(lista)
    archivo.write(nros)
    archivo.close()

def leerTabla(nombreTabla):
    archivo = open(nombreTabla,"r")
    diccionario={}
    for linea in archivo:
        lista = linea.split(",")
    for nro in lista:
        diccionario[nro]=False
    return diccionario

def jugar(diccionario, nro):
    if nro in diccionario:
        diccionario[nro]=True
    return diccionario


print("Bienvenido al juego Pozo Millonario")
tabla = input("Ingrese un nombre para su tabla")
crearTabla(tabla)
print("Se ha creado la tabla:",tabla)
tablaJuego = leerTabla(tabla+".txt")
aciertos = 0
while aciertos<8:
    aciertos = 0
    nro = input("Ingrese nro jugado:")
    tablaJuego = jugar(tablaJuego,nro)
    for k,v in tablaJuego.items():
        if v == True:
            jugar(tablaJuego,nro)
            aciertos+=1

if aciertos>=8:
    print("Ha ganado 1 pto extra")