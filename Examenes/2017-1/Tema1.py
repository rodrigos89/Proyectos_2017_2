#TEMA 1: Scrabble

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
puntuaciones = [2,4,4,3,2,5,3,5,2,8,6,12,4,2,2,4,9,2,2,2,2,5,5,8,5,9]

palabras = "cas*a*,S*ASTR*E*,R*EY*,A*ZOTE*"     #Cadena de entrada
listapalabras = palabras.split(",")             #Separa en una lista
listavalores = []

for pal in listapalabras:                       #Recorre la lista de palabras, pal es cada palabra
    sumaPuntuacion = 0
    valor = 0
    if pal.endswith("*"):                       #Valida que cada palabra termine en *, En el
        for letra in pal:                       #Recorre letra de cada palabra
            if letra.isupper():                 #Valida que la letra sea mayuscula
                indice = letras.index(letra)    #Obtiene el índice de la posición de la letra
                valor = puntuaciones[indice]    #Recupera el valor de la puntuación según el índice
                sumaPuntuacion+=valor           #Suma la puntuación de cada letra
            elif letra=="*":                    #Si letra es un *
                sumaPuntuacion += valor         #Suma nuevamente el último valor
        listavalores.append(sumaPuntuacion)     #Se agrega la suma de puntuaciones de la palabra a una lista
    else:                                       #Para casos donde no termina la palabra en *
        listavalores.append(sumaPuntuacion)     #Se agrega 0 para las palabras no válidas, y que no afecte la posición de las válidas
    print(pal,":",sumaPuntuacion)
mayorPuntuacion = listavalores.index(max(listavalores))

print("La palabra con mayor puntuación es:", listapalabras[mayorPuntuacion].replace("*",""))