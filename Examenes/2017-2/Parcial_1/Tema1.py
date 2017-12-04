#Ordenar actividades Navidad
import numpy as np

listaAct = ["pintar​ ​soldados", "hornear​ ​galletas", "armar​ ​muñecos", "cortar​ ​papel​ ​de​ ​regalo", "revisar"]
listaInicio = [300, 200, 1000, 560, 500]
listaDuracion = [200, 400, 441, 345, 700]
totalHoras = 1440

listaTotales = np.array(listaInicio, int) + np.array(listaDuracion) #Suma lista inicio y duración
listaActividades = [] #para guardar el listado de actividades

while totalHoras>0:
    mayor = listaTotales.argmax()
    if totalHoras == listaTotales[mayor]:
        listaActividades.append(listaAct[mayor])
        listaTotales[mayor] = -1
    elif totalHoras<listaTotales[mayor]:
        listaTotales[mayor] = -1

    totalHoras-=1

lineas = "+"+" -"*9+"+"
print(lineas+"\n|  Tareas del día  |\n"+lineas)

cont = 1
for actividad in listaActividades[::-1]:
    print("{0}. {1}".format(cont,actividad))
    cont+=1