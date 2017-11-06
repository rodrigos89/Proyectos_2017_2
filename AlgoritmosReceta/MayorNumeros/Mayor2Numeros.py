numero1 = int(input("Ingrese número 1: "))
numero2 = int(input("Ingrese número 2: "))

if numero1>numero2:
    print("%d es mayor que %d."%(numero1,numero2))
elif numero2>numero1:
    print("%d es mayor que %d." % (numero2, numero1))
else:
    print("%d y %d son iguales." % (numero1, numero2))