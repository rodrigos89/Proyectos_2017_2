#1. Indique la salida por pantalla del siguiente código. Justifique su respuesta.

f = ['a','c','z','m','k']
g = [3,4,5,6,5,7]
t = ''
for letra in f: #recorre cada letra de la lista f
    a = f.index(letra) #obtiene la posición de la letra en la lista
    b = g[:a] #slicing de g desde el inicio hasta la posición de la letra anterior
    t = t + (letra * len(b)) #concatena un producto que repite una letra el tamaño de b
print("1: ", t)

#2. Indique la salida por pantalla del siguiente código. Justifique su respuesta.

import numpy as np
vector = np.array([1, 5, 6, 6, 5, 2, 1, 3, 7, 9, 0, 0, 1, 4, 8])
print("2: ",np.unique(vector[vector % 2 == 0]).size) #encuentra los números pares, divisibles para 2 sin residuo,
                                            # luego deja una sola vez cada uno con unique.