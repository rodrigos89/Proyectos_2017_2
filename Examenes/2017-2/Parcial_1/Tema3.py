import numpy as np

tipoGasolina = np.array(['Regular', 'Extra', 'Súper','EcoPais','Premium'])
gasolineras = np.array(['Primax Alborada', 'PS Los Ríos', 'Mobil Cumbayá', 'Ceibos', 'Lutexsa'])
distrito = np.array(['distrito1', 'distrito3', 'distrito1', 'distrito3','distrito3'])
ciudades = np.array(['Guayaquil', 'Babahoyo' , 'Quito' ,'Guayaquil', 'Cuenca'])

filas = tipoGasolina.size
columnas = gasolineras.size

M = np.random.randint(234000,2000000,(filas, columnas),int)

print(M)

#1. Pida un tipo de gasolina por teclado y muestre por pantalla los nombres ​de todas las
# gasolineras que han vendido en el año menos​ ​del​ ​promedio​ ​de​ ​venta​ en galones para ese tipo

nombreGasolina = input("Ingrese nombre de Gasolina: ")

if nombreGasolina in tipoGasolina:
    gasolina = np.where(tipoGasolina==nombreGasolina)
    ventasGasolina = M[gasolina][0]
    promedio = ventasGasolina.mean()
    cualesGasolineras = np.where(ventasGasolina<promedio)
    listadoGasolineras = gasolineras[cualesGasolineras]
    #ventasGasolina = M[np.where(tipoGasolina==nombreGasolina)][0]
    #promedio = ventasGasolina.mean()
    print("Promedio de ventas:",promedio)
    #listadoGasolineras = gasolineras[np.where(ventasGasolina<promedio)]
    print("Gasolineras", listadoGasolineras)

#2. Pida una ciudad por teclado y calcule cuántas de sus gasolineras han vendido menos de 5
# millones​ de galones en total en el año, considerando todas las ventas de todos los tipos de gasolinas

transpuesta = M.transpose()
nombreCiudad = input("Ingrese una ciudad por Teclado: ")
if nombreCiudad in ciudades:
    posCiudad = np.where(ciudades==nombreCiudad)
    gasolineras = transpuesta[posCiudad]
    totalVentas = gasolineras.sum(axis=1)
    print("Total de ventas por Gasolinera:", totalVentas)
    cuantasGasolineras = np.where(totalVentas<5000000)[0].size
    print("El número de gasolineras que vendieron menos de 5 millones es:", cuantasGasolineras)

#3. Muestre por pantalla el nombre de la ciudad que más galones ha vendido en el año de
# gasolina tipo EcoPaís​ ​en el distrito distrito3​
posDistrito3 = np.where(distrito=="distrito3")
ciudadesD3 = ciudades[posDistrito3]
ciudadesD3_1vez = np.unique(ciudadesD3)
colEcoPais = np.where(tipoGasolina=="EcoPais")[0][0]
ecoPaisD3 = transpuesta[posDistrito3,colEcoPais][0]
totalCiudad = []
for ciudad in ciudadesD3_1vez:
    posCD3 = np.where(ciudadesD3 == ciudad)
    sumaCiudad = ecoPaisD3[posCD3].sum()
    print(ciudad+":",sumaCiudad)
    totalCiudad.append(sumaCiudad)
posMayor = totalCiudad.index(max(totalCiudad))
print("La ciudad del D3 con mayor ventas Ecopais es: ", ciudadesD3_1vez[posMayor])