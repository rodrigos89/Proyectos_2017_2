#Rodrigo Saraguro

#1.	Cree una función que obtenga el nombre de los equipos que irán a Copa Libertadores.
# El 1ero, 2do y 3ero que tengan más puntos (10 ptos).

def copaLibertadores(nombreArchivo):
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
        diccionario[ptos] = nombre
    puntos.sort(reverse=True)
    return (diccionario[puntos[0]],diccionario[puntos[1]],diccionario[puntos[2]])

#2.	Cree una función que obtenga los nombres de los equipos de la ciudad de Quito

def consultaEquiposCiudad(nombreArchivo, ciudadFiltrar, i):
    archivo = open(nombreArchivo)
    equipos=[]
    for linea in archivo:
        linea = linea.replace("*", ",")
        datos = linea.split(",")
        ciudad = datos[2]
        if ciudad == ciudadFiltrar:
            equipos.append(datos[i])
    return equipos

#3.	Cree una función que obtenga el total de goles de los equipos de Guayaquil (Gye). (5 ptos)
def totalGye(nombreArchivo, ciudad, i):
    lista = consultaEquiposCiudad(nombreArchivo,ciudad, i)
    for i in range (0,len(lista)):
        lista[i] = int(lista[i])
    return sum(lista)

print(copaLibertadores("2017.txt"))
print(consultaEquiposCiudad("2017.txt","Uio",1))
print(totalGye("2017.txt","Gye",8))