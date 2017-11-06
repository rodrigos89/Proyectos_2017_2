numero1 = int(input("Ingrese número 1: "))
numero2 = int(input("Ingrese número 2: "))
numero3 = int(input("Ingrese número 3: "))

if numero1>numero2 and numero1>numero3:
    mayor = numero1
elif numero2>numero1 and numero2>numero3:
    mayor = numero2
else:
    mayor = numero3

print("El mayor de %d, %d y %d es %d."%(numero1,numero2,numero3,mayor))