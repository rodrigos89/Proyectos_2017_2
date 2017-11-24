import numpy as np

#Imagine que la siguiente matriz corresponde a la venta en $ de productos de una tienda
#por 1 año. Las filas representan el producto, las columnas cada mes.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
          "Agosto", "Septiembre","Octubre", "Noviembre", "Diciembre"]

carnes = ["pollo", "res", "cerdo"]
complementos = ["arroz", "azúcar", "sal"]
tipoProd = ["Carnes", "Complementos"]
productos = carnes+complementos

ventas = np.random.randint(8,40,(len(productos),len(meses)), int) #matriz de enteros aleatorios de -4 al 20
print("Las compras de todo el año:\n", ventas)

#Una vez lista su matriz, y conociendo que representa cada fila y columna,
#responda las siguientes preguntas

#1. ¿Cuál fue la venta total de la tienda por mes y total anual?
totalMes = ventas.sum(axis=0) #calcula mes por columnas
for i in range(len(meses)): #para iterar de 0 a 11
    print(meses[i][0:3]+":\t$",totalMes[i]) #imprime cada mes con cada total del mes correspondiente
total = totalMes.sum() #Suma del año
print("Total \t${0}.".format(total))
print()
#2. ¿Cuál fue el mes que tuvo más ventas?
indMax = totalMes.argmax() #obtiene la posición del mes con más ventas
print("El mes con más ventas fue:", meses[indMax]) #Imprime el mes de acuerdo a esa posición obtenida
print()
#3. ¿Qué producto fue el que más se vendió los primeros 6 meses y cuánto?
corte6meses = ventas[:,0:6] #slicing todos los productos, meses: 0,1,2,3,4,5
sumaProd = corte6meses.sum(axis=1) #suma por filas=productos
#print(sumaProd)
posProdMasVent = sumaProd.argmax()
totalVenta = sumaProd.max()
print("El producto que más se vendió los primeros 6 meses fue {0} con un "
      "total de ${1}.".format(productos[posProdMasVent],totalVenta))
print()
#4. ¿En qué mes se vendieron menos carnes?
comprasCarnesxMes = ventas[0:len(carnes)].sum(axis=0) #suma por columna del slicing de las 3 primeras filas
#print(comprasCarnesxMes)
totalMenorCarnes = comprasCarnesxMes.min() #obtiene el menor del vector anterior
pos = comprasCarnesxMes.argmin() #obtiene la posición del mes menor
print("El mes en que se vendió menos carne fue en {0} con un "
      "total de ${1}.".format(meses[pos],totalMenorCarnes))
print()
#5. ¿Cual fue el promedio de ventas en Diciembre?
ventasDic = ventas[:,-1] #slicing todas las filas, última columna=Diciembre
promedioDic = ventasDic.mean() #calcula promedio
print("El promedio de ventas de Diciembre fue $%.2f"%(promedioDic)) #imprimiendo 2 decimales
#6. ¿Qué tipo de producto tuvo menos ventas los 3 últimos meses?
ventasProd = ventas[:,-3:] #slicing todas las filas, 3 últimas columnas
totalVentasxProd = ventasProd.sum(axis=1) #suma x filas
totalTipo= [totalVentasxProd[:len(carnes)].sum(),totalVentasxProd[-len(complementos):].sum()] #suma total por tipo producto
pos = totalTipo.index(min(totalTipo))
print()
print("El tipo de producto que menos ventas tuvo de Oct-Dic fue", tipoProd[pos])

#7. ¿Qué tipo de carne tuvo mayores ventas en enero?
ventasCarneEnero = ventas[:len(carnes),0] #filas 0,1,2 columna 0
posMayor = ventasCarneEnero.argmax() #Obtiene la pos de la carne con mayores ventas
ventasMayor = ventasCarneEnero.max() #Obtiene el valor de la carne con mayores ventas
print()
print("El tipo de carne con mayor ventas en enero fue {0} "
      "con un total de ${1}.".format(carnes[posMayor],ventasMayor))

#8. ¿Cuál de los 3 últimos productos tuvo menos ventas de enero a abril?
ventasProd4meses = ventas[-len(complementos):,0:4] #slicing 3 productos complemento de los 4 primeros meses
posProdMenor = ventasProd4meses.sum(axis=1).argmin() #el menor de la suma por producto
totProdMenor = ventasProd4meses.sum(axis=1).min()
print()
print("El producto con menos ventas de enero a abril fue {0} "
      "con un total de ${1}.".format(complementos[posProdMenor],totProdMenor))

#9. ¿Cual fue el promedio de ventas del producto que tuvo mayor ventas en el año?
ventasProd = ventas.sum(axis=1)
mayorVentasProd = ventasProd.argmax()
promedioVentasProd = ventas[mayorVentasProd].mean()
print()
print("El producto con mayor ventas fue {0} "
      "con un total de ${1}.".format(productos[mayorVentasProd],promedioVentasProd))

#10. ¿Cuantos productos vendieron menos de $275 al año, y cuáles fueron?
print()
#print("Total ventas x producto:",ventasProd)
cuales = np.where(ventasProd<275) #devuelve los indices de los productos que vendieron menos de 275
arrProd = np.array(productos,dtype="str") #transformando la lista de productos a un arreglo numpy de str
print("Los productos que vendieron menos de $275 en el año fueron:",arrProd[cuales],"cant:", len(cuales[0]))

#11. ¿Qué meses superaron las ventas de Diciembre?
ventasDic = totalMes[-1] #ultimo mes
posMeses = np.where(totalMes>ventasDic)[0] #donde el total del mes sea mayor al total ultimo mes
arrMeses = np.array(meses,dtype="str") #para extraer los nombres de los meses
print()
print("Los meses que superaron las ventas de Diciembre son:", arrMeses[posMeses])

#12. Obtenga el nombre de los productos y su promedio anual de ventas de aquellos
# productos que vendieron mas de $30 en Mayo
mediaProductos = ventas.mean(axis=1)
productosMayo = ventas[:,4]
indices = np.where(productosMayo>30)[0]
print(indices)
mediaAnual = mediaProductos[indices]
nombres = arrProd[indices]
print("Los productos que vendieron más de $30 en Mayo:", end="")
print(nombres)
print("Las medias de estos productos fue:", end="")
print(mediaAnual)