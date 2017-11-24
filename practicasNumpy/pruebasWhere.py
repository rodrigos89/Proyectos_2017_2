import numpy as np

matriz = np.random.randint(20,40,(3,4), dtype=int)

print(matriz)

b = np.where(matriz[matriz>30])
c = np.where(matriz>30)
d = matriz[c]

print("Presenta posición de elementos > 30:",b) #Elementos mayores a 30 array[elementos del 0 hasta n]
print("Presenta los indices f,c de los elementos > 30:",c)  #Índices de los elementos mayores a 30 (array de filas, array de columnas)
print("Presenta los valores de los elementos > 30:",d) #Valores de los elementos mayores a 30


#Segunda Forma
matriz2 = np.random.randint(20,40,(3,4), dtype=int)
print(matriz2)
e = matriz2>30
f = matriz2[matriz2>30]

print("Presenta matriz booleana si es > 30:\n",e) #Valores de los elementos mayores a 30
print("Presenta los valores que cumplen la condición >30:\n",f)