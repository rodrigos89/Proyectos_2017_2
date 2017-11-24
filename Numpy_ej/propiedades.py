import numpy as np

arr_aleat = np.random.randint(-4,20,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz:\n", arr_aleat)

print("Forma:", arr_aleat.shape)
print("Elementos:", arr_aleat.size)
print("Dimensiones:", arr_aleat.ndim)
print("Tipo:", arr_aleat.dtype)