#Tema 3, dada la siguiente lista
import random as rd

L = [12,9,1,3,10,20,5,1]
suma = 0

while suma<18:
    suma = 0
    for i in range (3):
        pos = rd.randint(0,len(L)-1)
        print(pos, L[pos])
        suma+= L[pos]


print(suma)


stars = ['Ron', 'Albus Dumbledore', 'Hermione', 'Harry Potter', 'Hagrid', 'Voldemort']

print(stars[-4:-2])

print(stars[3][0:stars[3].find(" ")]+stars[1][5:])