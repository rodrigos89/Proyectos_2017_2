#En esta práctica se requiere que el usuario personalice su estado de politéchicos
#reemplazando los datos de Ricardo

estado = "Mi nombre favorito es Ricardo, soy de la ciudad de Portoviejo, tengo 23 años. " \
         "Estudio la carrera Lenguas, actualmente curso el nivel 400. " \
          "Y estoy buscando ..."

nombre = input("Ingrese nombre:")
ciudad = input("Ingrese ciudad:")
fechaNac = input("Ingrese año de Nacimiento:")
edad = 2017-int(fechaNac)

#1. Solicite al usuario los datos que faltan
carrera = input("Ingrese carrera:")
nivel = input("Ingrese nivel:")
buscando = input("Ingrese lo que está buscando:")

#2. Realice slicing de las partes que le sirven y concatene
#estado = estado[0:13]+nombre+estado[20:42]+ciudad+estado[52:60]+str(edad)+estado[62:67] #faltan los demás slicing
#print(estado)

#Una solución sin necesidad de conocer las posiciones
estado = estado.replace("Ricardo", nombre.title()).replace("Portoviejo", ciudad.title()).replace("23", str(edad))
estado = estado.replace("Lenguas", carrera.title()).replace("400",nivel).replace("...", buscando+".")

#4. Imprima el nuevo estado
print(estado)

'''5. Una vez actualizado el estado, valide que los datos sean correctos.
   Por cada validación debe imprimir True o False'''
#5.1. Valide que el nombre esté bien escrito: Mayuscula la primera letra, todo lo demás min
validacion1 = nombre.istitle()
print("Validación 1: ", validacion1)

#5.2. Valide que el nombre no tenga ningún número
validacion2 = nombre.isalpha()
print("Validación 2: ", validacion2)

#5.3. Valide que la edad sólo tenga números
validacion3 = fechaNac.isdigit() and str(edad).isdigit()
print("Validación 3: ", validacion3)

#5.4. Valide que la carrera tenga sólo letras
validacion4 = carrera.isalpha()
print("Validación 4: ", validacion4)

#5.5. Valide que la ciudad no sea igual que el nombre
validacion5 = nombre!=ciudad
print("Validación 5: ", validacion5)

#5.6. Valide que el nivel ingresado sea un número
validacion6 = nivel.isdigit()
print("Validación 6: ", validacion6)

#5.7. Valide que la ultima frase de lo que busca tenga más de 15 caracteres
validacion7 = len(buscando)>15
print("Validación 7: ", validacion7)

#5.8. Si ha pasado todas las validaciones, imprima "Todos los datos son válidos"
print("Validación Todas: ", validacion1 & validacion2 & validacion3)