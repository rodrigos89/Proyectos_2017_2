vocales = ["a","e","i","o","u"]

frase = input("Ingrese palabra o frase a validar: ").lower()

#Para dejar una sola forma de separación. espacio en blanco y tratar solo minusculas
frase = frase.replace("."," ")

#Generando una lista con cada palabra reconocida, basada en el espacio en blanco
palabras = frase.split()


#Para seleccionar los elementos que no contengan número
contGeneral=0
for palabra in palabras:
    if(palabra.isalpha()):
        contVocal = 0
        contCons = 0
        for letra in palabra:
            if letra in vocales:
                contVocal += 1  # Para sumar las vocales encontradas
            else:
                contCons += 1  # Para sumar lo que no es vocal
        if contVocal == contCons:
            contGeneral += 1

print(contGeneral)