
#1. Escriba un programa que calcule el valor absoluto de un número.
# El programa solicita al usuario que ingrese un dato y como resultado
# muestra el valor absoluto del dato ingresado. Archivo a llevar: absoluto.py

#Valide que el valor sea un número entero.
valor = "a"
while (not valor.isdigit()):
    valor = input("Ingrese número entero:")
    nro = int(valor)
    if nro < 0:
        valorabs = nro * -1
    else:
        valorabs = nro
print("El valor absoluto de {0} es {1}.".format(valor, valorabs))
print()



#2. Escriba un programa que implemente el juego de adivinar el número.
# El número inicial debe ser generado al azar (random del 1 al 25).
# La respuesta debe ser ingresada por teclado (input).
# Si la respuesta coincide con el número generado al azar presente el mensaje: "ADIVINASTE“.
# Caso contrario: "HOY NO ES TU DÍA, VUELVE A INTENTARLO MÁS TARDE." Archivo a llevar: adivinar.py
#El usuario ahora tiene 5 oportunidades para adivinar



















import random as al

aleatorio = al.randint(1,25)
nro = int(input("Ingrese un número del 1 al 25:"))
if nro == aleatorio:
    print("ADIVINASTE")
else:
    print("HOY NO ES TU DÍA, VUELVE A INTENTARLO MÁS TARDE.")
print()










#3. Escriba un programa para una tienda que cobra $12 por artículo si el usuario compra 10 artículos o menos.
# Si el usuario compra entre entre 11 y 49 artículos, el costo por artículo es de $10.
# Si el usuario compra 50 o más artículos el costo por artículo es de $7.
# Escriba un programa que pida al usuario cuantos items el está comprando e imprima el costo total de la compra.
# Archivo a llevar: tienda.py
#1. Agregar datos de cliente
# Si la suma de todo es mayor a $300 hacer un descuento del 5%

nroArt = int(input("Ingrese nro de artículos:"))
if nroArt<=10:
    precio = 12
elif nroArt>10 and nroArt<=49:
    precio = 10
else:
    precio = 7
total = nroArt*precio
print("El costo total de la compra de {0} artículos es: {1}.".format(nroArt,total))
print()

#4. Escriba un programa que permita agregar horas extras a un trabajador.
# Siempre y cuando el empleado haya realizado entre 0 a 10 horas el costo por hora será de $8,
# si el rango es de 11 a 20 horas el costo es de $10, si supera las 20 horas el costo es de $15.
# Calcule el sueldo total, deduzca el 9.35% de aporte al IESS y si supera los $980
# presente un mensaje "Debe hacer su declaración de Impuesto a la Renta",
# caso contrario "No requiere hacer declaración al SRI". Archivo a llevar: sueldo.py

sueldo = float(input("Ingrese sueldo:"))
horasExtra = int(input("Ingrese nro de horas extra:"))
if 0<=horasExtra<=10:
    costo = 8
elif horasExtra<= 11 and horasExtra<=20:
    costo = 10
else:
    costo = 15

totalHE = horasExtra*costo
sueldoSub = sueldo+totalHE
aporte = sueldoSub*0.0935
sueldoNeto = sueldoSub-aporte
print("El sueldo neto del empleado es: ", sueldoNeto)
if sueldoNeto>=980:
    mensaje = "No requiere hacer declaración al SRI"
else:
    mensaje = "Debe hacer su declaración de Impuesto a la Renta"
print(mensaje)
print()
#5. Escriba un programa que permita obtener la nota cualitativa de la materia Fundamentos de Programación.
# En base a los rangos establecidos en la parte inferior.
# Si el usuario ingresa un valor no válido de puntuación presentar Incorrecto. Archivo a llevar: calificacion.py
'''Puntuación Calificación
   >= 9       Sobresaliente
   >= 8       Notable
   >= 7       Bien
   >= 6       Suficiente
   < 6        Insuficiente'''

notaStr = input("Ingrese nota de FP: ")

if notaStr.isdigit():
    nota = float(notaStr)
    if nota>=9 and nota<=10:
        cualitativa = "Sobresaliente"
    elif nota>=8 and nota <9:
        cualitativa = "Notable"
    elif nota>=7 and nota <8:
        cualitativa = "Bien"
    elif nota>= 6 and nota<7:
        cualitativa = "Suficiente"
    elif nota<6:
        cualitativa = "Insuficiente"
    mensaje = "La nota {0} en la escala cualitativa significa {1}.".format(nota, cualitativa)
else:
    mensaje = "Ha ingresado una nota no válida"

print(mensaje)