import numpy as np

arr_lista = np.array([3,4,5,9,-2], int) #vector de enteros a partir de una lista
print("Vector 1:\n",arr_lista)

arr_listaA = np.array([[3,4,5],[-1,9,3]]) #matriz de floats a partir de lista anidada
print("Matriz 1:\n", arr_listaA)

arr_rango = np.arange(3,19,2) #vector de enteros a partir de un rango y saltos
print("Vector 2:\n", arr_rango)

arr_ceros = np.zeros((3), int) #vector de 0s
print("Vector 3:\n", arr_ceros)

arr_unos = np.ones((5,7), int) #matriz de 1s
print("Matriz 2:\n", arr_unos)

arr_lleno = np.full((4,3), 10, int) #matriz de 10
print("Matriz 3:\n", arr_lleno)

arr_aleat = np.random.randint(-4,20,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz 4:\n", arr_aleat)

arr_vacia = np.empty((5,6), dtype=str) #matriz vacía
print("Matriz 5:\n", arr_vacia)

arr_diag = np.eye(4,6,k=2) #Crea una matriz de 0s con una diagonal de 1s que inicia en la pos 2 de columnas
print("Matriz 6:\n", arr_diag)
