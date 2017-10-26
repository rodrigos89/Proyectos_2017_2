palabra= "helicoptero"
saludo = "AHORCADO".center(30, "*")
print(saludo)
print("Adivine la palabra basado en las siguientes letras:")
inicio = 0
mitad = len(palabra)//2
fin = -1
nro_guiones = len(palabra[mitad:fin])-1
print(palabra[inicio]+
      "_ "*(mitad-1) + palabra[mitad] + "_ "*(nro_guiones) +palabra[fin])
ingresada=input("Ingrese palabra: ")
print(palabra == ingresada)
