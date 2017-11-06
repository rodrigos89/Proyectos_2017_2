#En este ejemplo se ingresa un número determinado de valores enteros para compararlos y obtener el mayor.
#SE VALIDA si el límite y cada uno de los valores a comparar son enteros


validoLim = True
mayor = 0
while validoLim:
    limite = input("Ingrese límite:")
    if(limite.isdigit()):
        validoLim = False
        for e in range(int(limite)):
            numeroComp = ''
            validoNro = False
            while not validoNro:
                numeroComp = input("Ingrese número %d:"%(e+1))
                validoNro=numeroComp.replace("-","").isdigit()
                if(validoNro and int(numeroComp)>mayor):
                    mayor = int(numeroComp)

print("El número mayor ingresado fue:",mayor)