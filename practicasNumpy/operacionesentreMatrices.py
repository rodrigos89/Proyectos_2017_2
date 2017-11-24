import numpy as np

mat_aleat = np.random.randint(8,40,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz 1:\n", mat_aleat)

mat_aleat2 = np.random.randint(1,25,(5,6), int) #matriz de enteros aleatorios de -16 al 0
print("Matriz 2:\n", mat_aleat2)

matSuma = mat_aleat+mat_aleat2
#igual a np.add(mat_aleat, mat_aleat2)
print("Matriz suma:\n", matSuma)

vecConsec = np.arange(1,12,2) #vector de numeros del 1 al 11 de 2 en 2
print("Vector arange:\n", vecConsec)

matResta = matSuma-vecConsec
# igual a np.substract(matSuma,vecConsec)
print("Matriz restante:\n", matResta)

matMult = matResta*vecConsec #Multiplica elemento por elemento de matResta * vecConsec
# igual a np.multiply(matSuma,matResta)
print("Matriz multiplicada:\n", matMult)

matProd = matResta.dot(vecConsec) #Producto de la matriz Resta con vecConsec union de multiply + suma por filas
print("Matriz producto:\n", matProd)

matDiv = matSuma/vecConsec #División de matSuma para vector vecConsec
print("Matriz dividida:\n", matDiv)

matRaiz = np.sqrt(matMult) #Raiz de los elementos de matMult
print("Matriz raiz:\n", matRaiz)
