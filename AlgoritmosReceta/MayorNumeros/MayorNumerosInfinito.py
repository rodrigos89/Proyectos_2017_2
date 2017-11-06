#En este ejemplo se ingresa un número determinado de valores enteros para compararlos y obtener el mayor.
#No se valida si los valores son enteros, así que podría dar error si el usuario ingresa mal los valores

print("Bienvenido")
print("Puede comparar un nro ilimitado de números hasta que escriba no")
nro = ""
mayor = 0
acumul = 1
while nro.strip().lower()!="no":
    nro = input("Ingrese número %d: "%acumul)
    if nro.replace("-","").isdigit():
        nroComp = int(nro)
        acumul +=1
        if(nroComp>mayor):
            mayor = nroComp
print("El número mayor ingresado fue:",mayor)