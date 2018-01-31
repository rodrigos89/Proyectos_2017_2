
def armarDiccionario(nombreArchivo):
    notas = {}
    archivo = open(nombreArchivo, "r")
    for linea in archivo:
        lineaLista = linea.replace("|",",").replace("-", ",")
        lista = lineaLista.split(",")
        estudiante = {lista[0]:[lista[2],lista[3],lista[4]]}
        if lista[1] in notas:
            notas[lista[1]][lista[0]]= [lista[2],lista[3],lista[4]]
        else:
            notas[lista[1]]=estudiante
    print(notas)
    archivo.close()

armarDiccionario("2018.txt")