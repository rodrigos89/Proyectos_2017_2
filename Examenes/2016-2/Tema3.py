transacciones = [ 'centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013',
                  'centro|Malecon2000|natacion|chaleco-Fins|110.92|01-02-2014',
                  'sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014',
                  'centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015',
                  'norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016',
                  'sur|CityMall|futbol|zapatos-Adidas|105.34|13-05-2016']


# Tres listas(sur,centro,norte) cuyos elementos son los nombres únicos de las tiendas: una lista por cada sector.

lista_centro = []
lista_sur = []
lista_norte = []

for elementos in transacciones:
    lista_transacciones = elementos.split("|")
    if("centro" in lista_transacciones):
        if lista_transacciones[1] not in lista_centro:
            lista_centro.append(lista_transacciones[1])
print("Las tiendas del centro son:", lista_centro)


for elementos in transacciones:
    lista_transacciones = elementos.split("|")
    if("sur" in lista_transacciones):
        if lista_transacciones[1] not in lista_sur:
            lista_sur.append(lista_transacciones[1])
print("Las tiendas del sur son:", lista_sur)

for elementos in transacciones:
    lista_transacciones = elementos.split("|")
    if("norte" in lista_transacciones):
        if lista_transacciones[1] not in lista_norte:
            lista_norte.append(lista_transacciones[1])
print("Las tiendas del norte son:", lista_norte)


# El total de ventas de los productos Adidas en el mes de mayo del año ingresado por teclado.
print()
anio = input("Ingrese año para generar reporte: ")
venta_adidas = 0
for elementos in transacciones:
    lista_transacciones = elementos.split("|")
    if("adidas" in lista_transacciones[3].lower() and lista_transacciones[5].endswith("05-"+anio)):
        venta_adidas += float(lista_transacciones[4])

print("El total de ventas de Adidas es:", venta_adidas)