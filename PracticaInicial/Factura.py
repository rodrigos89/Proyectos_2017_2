#practica creada por Rodrigo Saraguro
#11-10-2017

cliente = input("Ingrese nombre del cliente:")
ruc = input("Ingrese el RUC:")
nombreProd1 = input("Ingrese nombre Producto 1:")
precioUnitario1 = float(input("Ingrese el precio:"))
cant1 = int(input("Ingrese la cantidad:"))
subtotal1 = precioUnitario1*cant1
nombreProd2 = input("Ingrese nombre Producto 2:")
precioUnitario2 = float(input("Ingrese el precio:"))
cant2 = int(input("Ingrese la cantidad:"))
subtotal2 = precioUnitario2*cant2
subtotalGeneral = subtotal1+subtotal2
#Aqui estoy calculando el iva de mi compra
iva = subtotalGeneral*0.12
totalPagar = subtotalGeneral+iva

print()
print("*** Mi primer Sistema de Facturación ***")
print("Cliente:",cliente)
print("RUC:",ruc)
print("Nro. Producto\t\tP.Unit\t Cant\t Subtotal")
print("1. \t %s \t%f\t %i\t %f"%(nombreProd1,precioUnitario1,cant1,subtotal1))
print("2. \t %s \t%f\t %i\t %f"%(nombreProd2,precioUnitario2,cant2,subtotal2))
print("Subtotal: \t \t \t \t \t ",subtotalGeneral)
print("Impuestos: \t \t \t \t \t ",iva)
print("Total a pagar: \t \t \t \t ", totalPagar)