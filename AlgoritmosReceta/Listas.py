puntuaciones = [20,23,34,100,3, 32.3, 99, 25, 45, 35, 47]
print(len(puntuaciones))
puntuaciones+=[23,56]
print(puntuaciones)
puntuaciones[0] =30
print(puntuaciones)
mayor = max(puntuaciones)
suma = sum(puntuaciones)/len(puntuaciones)
print(suma)
puntuaciones = puntuaciones*2
print(puntuaciones)

puntuaciones.insert(0,[23,45])
print(puntuaciones)
puntuaciones.extend([23,45])
print(puntuaciones)

a = puntuaciones.pop(-1)

print(a)