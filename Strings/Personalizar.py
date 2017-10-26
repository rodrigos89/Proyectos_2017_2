#En esta práctica se requiere que el usuario personalice su estado de politéchicos
#reemplazando los datos de Ricardo

estado = "Mi nombre es %s, soy de la ciudad de %s, tengo %f años. " \
         "Estudio la carrera %s, actualmente curso el nivel %s. " \
          "Y estoy buscando %s"

nombre = input("Ingrese nombre:")
ciudad = input("Ingrese ciudad:")
fechaNac = input("Ingrese año de Nacimiento:")
edad = 29.8
carrera = input("Ingrese carrera:")
nivel = input("Ingrese nivel:")
buscando = input("Ingrese lo que está buscando:")


print(estado%(nivel, buscando, edad, carrera, nombre, ciudad)) #Forma 1


estado = "Mi nombre es {0}, soy de la ciudad de {1}"

print(estado.format(nombre,ciudad)) #Forma 2

