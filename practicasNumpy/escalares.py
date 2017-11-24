import numpy as np

arr_aleat = np.random.randint(-4,20,(5,6), int) #matriz de enteros aleatorios de -4 al 20
print("Matriz original:\n", arr_aleat)
arrEsc1 = arr_aleat*2 #Multiplica todos los elementos de la matriz x 2
print("Matriz * 2:\n", arrEsc1)

arr_aleat+=10
print("Matriz +10:\n", arr_aleat)

arrEsc1[-1] = 5 #La última fila de la matriz arrEsc1 se reemplazará por 5
print("Matriz ultima fila a 5:\n", arrEsc1)

arrEsc1[0:2,-3:] += 10 #Las primeras 2 filas y las 3 últimas col sumarles 10
print("Matriz a 10:\n", arrEsc1)

arrDiv = arrEsc1//2
print("Matriz // 2:\n", arrDiv)

arrPot = arrDiv**3
print("Matriz al cubo:\n", arrPot)