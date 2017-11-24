import numpy as np

arr_aleat = np.random.randint(-4,20,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz:\n", arr_aleat)

ult_ele = arr_aleat[-1,-1] #obtiene el último elemento de fila y columna, es decir punta inferior izq
print("El último elemento es:\n", ult_ele)

colfinal = arr_aleat[:,-1] #obtiene todas las filas, con la última columna
print("Slicing de última columna:\n", colfinal)

colinicial = arr_aleat[:,0] #obtiene todas las filas, con la primera columna
print("Slicing de primera columna:\n", colinicial)

filaInicial = arr_aleat[0] #obtiene la fila 0, todas las columnas
#tambien podría usar [0,:]
print("Slicing de primera fila:\n", filaInicial)

filaFinal = arr_aleat[-1,:] #obtiene la fila -1, todas las columnas
#tambien podría usar [-1]
print("Slicing de última fila:\n", filaFinal)

filas2 = arr_aleat[0:2,:] #obtiene las 2 primeras fila (0,1) y todas las columnas
#otra solución sería [0:2], si no necesito especificar columnas
print("Slicing de las 2 primeras filas:\n", filas2)

colmitad = arr_aleat[:,2:4] #obtiene todas las filas, columnas de la 2 a 3 (el 4 se excluye)
print("Slicing de las 2 columnas del centro:\n", colmitad)