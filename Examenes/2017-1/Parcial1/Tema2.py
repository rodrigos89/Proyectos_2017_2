import numpy as np
espana = ['elrubiusOMG', 'VEGETTA777', 'Pablo Alborán']
ecuador = ['enchufetv', 'Kreizivoy', 'DavidCRG']
mexico = ['Yuya', 'Werevertumorro']

paises = np.array(["España", "Ecuador", "México"])
youtubers = np.array(espana+ecuador+mexico)

'''Considere las siguientes métricas:
● Popularidad = número de suscriptores
● Visibilidad = número reproducciones / número de suscriptores'''

matriz = np.random.randint(100000, 2000000, (4,youtubers.size))
suscripciones = matriz[0]
reproducciones = matriz[1]
ganMensuales = matriz[2]

#1. Nombres de usuarios de los youtubers con mayor  visibilidad  en cada país.  Tipo de dato de respuesta: lista de strings .


visibilidadYoutubers = reproducciones/suscripciones
visEspana = visibilidadYoutubers[:len(espana)]
visEcuador = visibilidadYoutubers[len(espana):-len(mexico)]
visMexico = visibilidadYoutubers[-len(mexico):]

youtuberEspana = np.array(espana)[np.argmax(visEspana)]
youtuberEcuador = np.array(ecuador)[np.argmax(visEcuador)]
youtuberMexico = np.array(mexico)[np.argmax(visMexico)]

print(matriz)
#print(visibilidadYoutubers)
print("El mejor youtuber de España es:",youtuberEspana)
print("El mejor youtuber de Ecuador es:",youtuberEcuador)
print("El mejor youtuber de México es:",youtuberMexico)

#2. El nombre del país del youtuber con la mayor  visibilidad .
#  Tipo de dato de la respuesta: string

mejoresYoutubers = np.array([youtuberEspana, youtuberEcuador,youtuberMexico])
pais = paises[mejoresYoutubers.argmax()]
print("El país del youtuber con mayor velocidad es:", pais)

#3. Cuántos youtubers de España tienen más suscriptores que el youtuber más  popular  de América (Ecuador y México).
# Tipo de dato de respuesta: valor entero

masPopularAmerica = matriz[0,len(ecuador):].max() #el que tiene más suscriptores
suscriptEspana = matriz[0,:len(espana)]
quienesEspana = suscriptEspana>masPopularAmerica
cuantosEspana = quienesEspana.sum()
print("El numero de Youtubers de España con más suscriptores que el popular de América son:", cuantosEspana)

#4. El número promedio de reproducciones de los youtubers con más de 1’000,000 de suscriptores.
# Tipo de dato de respuesta: valor entero.

youtubersMillon = suscripciones[suscripciones>100000].mean()
print("El promedio de los youtubers con más de 1’000,000 de suscriptores es:", youtubersMillon.round()) #para que sea entero redondear con round

#5. Cuántos youtubers de Ecuador hay en cada categoría. La categoría se calcula en base a la siguiente tabla:
# Rango de visibilidad      Categoría
#   0.0 a 0.25                  -1
#   0.26 a 0.70                 0
#   > 0.71                      1
# Tipo de dato de respuesta: ndarray de enteros.

#print(visEcuador)
cate_1 = (visEcuador>0) & (visEcuador<0.25)
cate0 = (visEcuador>0.26) & (visEcuador<0.70)
cate1 = (visEcuador>0.71)
print("Categoria -1",cate_1.sum())
print("Categoria 0",cate0.sum())
print("Categoria 1",cate1.sum())

#6. El  país  que generó más ganancias mensuales y el  país  que generó menos ganancias mensuales.
# Luego muestre el siguiente mensaje reemplazando los datos apropiadamente:
# El país X generó Z% más de ganancias mensuales que el país Y.
gananciasPaises = np.array([ganMensuales[:len(espana)].sum(),ganMensuales[len(espana):-len(mexico)].sum(),ganMensuales[-len(mexico):].sum()])
posGX = gananciasPaises.argmax()
posGY = gananciasPaises.argmin()
GX = gananciasPaises.max()
GY = gananciasPaises.min()
porcentaje = (GX - GY)/GY * 100
print("El país {0} generó {1}% más de ganancias mensuales que el país {2}.".format(paises[posGX],porcentaje.round(2),paises[posGY]))
