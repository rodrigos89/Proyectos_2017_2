#Rodrigo Saraguro

#1.	Cree una función que obtenga el nombre y ciudad de los equipos que descenderán.
# El último y penúltimo que tengan menos puntos (10 ptos).

def descienden(nombreArchivo):
    archivo = open(nombreArchivo)
    puntos=[]
    diccionario = {}
    for linea in archivo:
        linea = linea.replace("*",",")
        datos = linea.split(",")
        ptos = int(datos[3])
        nombre = datos[1]
        ciudad = datos[2]
        puntos.append(ptos)
        diccionario[ptos] = [nombre,ciudad]
    puntos.sort()
    return (diccionario[puntos[0]],diccionario[puntos[1]])

#2.	Cree una función que obtenga un listado de los equipos que no son de Quito (Uio) ni Guayaquil (Gye). (5 ptos)
def nosonQuitoGye(nombreArchivo):
    archivo = open(nombreArchivo)
    equipos=[]
    for linea in archivo:
        linea = linea.replace("*", ",")
        datos = linea.split(",")
        ciudad = datos[2]
        equipo = datos[1]
        if ciudad != "Gye" and ciudad!="Uio":
            equipos.append(equipo)
    return equipos

#3.	Cree una función que devuelva el total de goles marcados a favor (GF) de todos los equipos de Quito (Uio). (5 ptos)
def golesQuito(nombreArchivo):
    archivo = open(nombreArchivo)
    golesT=[]
    for linea in archivo:
        linea = linea.replace("*", ",")
        datos = linea.split(",")
        goles = int(datos[-3])
        ciudad = datos[2]
        if ciudad=="Uio":
            golesT.append(goles)
    return sum(golesT)

print(descienden("2017.txt"))
print(nosonQuitoGye("2017.txt"))
print(golesQuito("2017.txt"))