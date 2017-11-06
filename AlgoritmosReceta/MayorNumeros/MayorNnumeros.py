#En este ejemplo se ingresa un número determinado de valores enteros para compararlos y obtener el mayor.
#No se valida si los valores son enteros, así que podría dar error si el usuario ingresa mal los valores

mayor = 0
limite = int(input("Ingrese límite: "))
for e in range(limite):
    nroComp = int(input("Ingrese número: "))
    if(nroComp>mayor):
        mayor = nroComp
print("El número mayor ingresado fue:",mayor)