import numpy as np

mat_aleat = np.random.randint(8,40,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz:\n", mat_aleat)

sumaTotal = mat_aleat.sum() #Suma de todos los elementos de la matriz

matCol = mat_aleat.sum(axis=0) #Suma por columnas de la matriz
print("Suma por columnas:\n", matCol) #vector de la suma de cada columna


matFil = mat_aleat.sum(axis=1) #Suma por filas de la matriz
print("Suma por filas:\n", matFil) #vector de la suma de cada fila

matFilEsp = mat_aleat[:3,-2:].sum(axis=1) #Suma por filas del slicing
print("Suma de slicing [:3,-2:]:\n", matFilEsp)

sumaTotal = mat_aleat.mean() #Media o promedio de todos los elementos de la matriz

matCol = mat_aleat.mean(axis=0) #Media por columnas de la matriz
print("Media por columnas:\n", matCol) #vector de la media de cada columna


matFil = mat_aleat.mean(axis=1) #Media por filas de la matriz
print("Media por filas:\n", matFil) #vector de la media de cada fila


matFilEsp = mat_aleat[-2:,0:3].mean(axis=0) #Media por columnas del slicing
print("Media de slicing [-2:,0:3]:\n", matFilEsp)


matFil = mat_aleat.sum(axis=1).mean() #Media de la suma por filas
print("Media por filas:\n", matFil) #cantidad promediada

matFil = mat_aleat.mean(axis=0).sum() #Suma de las medias por columnas
print("Suma de la media por col:\n", matFil) #cantidad sumada