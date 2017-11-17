'''
La lista mostrada en el ejemplo contiene los URLs de diferentes sitios Web que han sido visitados.
Los URLs normalmente se repiten y corresponden algunas veces a universidades de Ecuador y otros países.
Note que los URLs no diferencian entre mayúsculas y minúsculas.
Por ejemplo:
 www.espol.edu.ec y  www.ESPOL.edu.EC
corresponden al mismo sitio.

'''

lista = ["www.espol.edu.ec", "www.google.com", "www.sri.gob.ec", "www.fiec.espol.edu.ec",
         "www.uess.edu.ec", "www.FIEC.espol.edu.ec", "www.fict.espol.edu.ec", "www.fcnm.Espol.edu.ec",
         "www.ucsg.edu.ec", "www.Stanford.edu", "www.harvard.edu", "www.stanford.edu", "www.UCSG.edu.ec",
         "www.google.com.ec", "www.facebook.com", "www.opensource.org", "www.educacionbc.edu.mx"]

'''
Escriba un programa en Python que dada una lista realice lo siguiente :

a. Muestre los nombres o siglas de las universidades que aparecen en la lista (sin repetir).
Del el ejemplo mostrado, la salida sería:
1.) ESPOL
2.) UESS
3.) UCSG
4.) STANFORD
5.) HARVARD
6.) EDUCACIONBC
'''
listaU = []
listaUEc = []
for url in lista:
    datosUrl = url.split(".")
    if "edu" in datosUrl:
        pos = datosUrl.index("edu")-1
        universidad = datosUrl[pos].upper()
        if universidad not in listaU:
            listaU.append(universidad)
            if "ec"==datosUrl[-1]:
                listaUEc.append(universidad)
#forma1
for univ in range(len(listaU)):
    print("{0}.) {1}".format(univ+1,listaU[univ]))
print()
#forma2
cont=1
for univ in listaU:
    print("{0}.) {1}".format(cont,univ))
    cont+=1
print()
#forma3
cont = 0
while cont<len(listaU):
    print("{0}.) {1}".format(cont + 1, listaU[cont]))
    cont+=1

'''
b. Muestre la cantidad y los nombres/siglas de universidades de Ecuador que aparecen en la lista.
Del ejemplo mostrado, la salida sería:
En la lista aparecen 3 universidades de Ecuador
1.) ESPOL
2.) UESS
3.) UCSG
'''
print()
for univ in range(len(listaUEc)):
    print("{0}.) {1}".format(univ+1,listaUEc[univ]))
print()


'''
Dado un usuario y el nombre o sigla de la universidad, imprima el correo electrónico asignado.
Por ejemplo:
Ingrese el usuario: rasarag
Ingrese el nombre/sigla de la universidad: ESPOL
El correo electrónico del usuario es: rasarag@espol.edu.ec
'''
usuario = input("Ingres el usuario:").lower()
dominio = input("Ingrese sigla de la Universidad:").upper()
if dominio in listaU:
    correo = usuario+"@"+dominio.lower()+".edu.ec"
    print(correo)


