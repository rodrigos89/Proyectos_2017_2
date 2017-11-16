'''En ESPOL ha sucedido un gran problema el último fin de semana:
un hacker recientemente ha accedido a la base de datos de credenciales
de usuarios ESPOL y ha modificado las contraseñas de todos los usuarios.
Es por ello que, el profesor de Fundamentos de Programación Par 19
solicita a sus estudiantes resolver el problema suscitado. A pesar de todo
el caos que se vive en ESPOL, el Equipo de Tecnologías ha logrado recuperar
una copia del mes de octubre de la mayoría de usuarios y contraseñas ESPOL.
'''

baseHackeada = [[201023847, 'Carlos Agila', 'cagila@espol.edu.ec', 'cagila', 1234],
                [201390384, 'Bot', 'correo@bot.ep', 'bot', 293848],
                [201123453, 'María Cedeño', 'mcedeno@espol.edu.ec', 'mcedeno', 1234],
                [201323847, 'José Perez', 'joseperez@gmail.com', 'jperez', 2938],
                [201391928, 'Bot', 'correo@bot.ep', 'bot', 29393]]

copiaOctubre = [['cagila', 'msu12h2'], ['rasarag', 'smsossj23'],['mcedeno', '2121jdjd'],
                ['lisme', 'ksmk222m'],['mmaza', '29ksj34'],['jperez', 'ksm334m']]

'''Usando la copia del mes de octubre realizar las siguientes instrucciones:
a)	Actualizar las contraseñas disponibles de copiaOctubre a baseHackeada, creando una copia independiente. (5 ptos)
b)	Borrar los usuarios de baseHackeada que no existan en copiaOctubre (5 ptos)
c)	Generar una lista de usuarios faltantes que consten en copiaOctubre y no en la baseHakeada, con miras a conocer cuales también ha borrado el hacker. (2 ptos extra)
'''

#LITERAL A
#copia independiente
baseHackeada1 = baseHackeada.copy()

for usuarios in copiaOctubre: #recorre la copia
    for datos in baseHackeada1: #recorre la base
        if usuarios[0]==datos[3]: #compara si el usuario (pos 0) existe en la base (pos 3)
            datos[4]=usuarios[1]    #si existe, se actualiza la contraseña (pos 4)
print(baseHackeada1)            #imprime la base actualizada

#LITERAL B
listaborrar = []    #crea una lista para agregar todos los índices a borrar
for datos in baseHackeada:     #recorre la base hackeada
    encontrado=False           #para validar si no fue encontrado el usuario
    for usuarios in copiaOctubre:      #recorre la copia
        if datos[3] == usuarios[0]: #Si el usuario fue encontrado en algun elemnto de la copia cambia a True
            encontrado = True
    indice = baseHackeada.index(datos) #recupera el índice de la sublista
    if indice not in listaborrar and encontrado==False: #Si el indice aun no se agrega y no fue encontrado
        listaborrar.append(indice)                      #se agrega el índice

print("Elementos a borrar:",listaborrar)                #imprimiendo lista de índices a borrar

listaborrar.sort(reverse=True) #ordenando de mayor a menor, porque si primero se eliminan los menores,
                                # los mayores ya cambiarían de posición y no existe tal posición
for i in listaborrar: #recorre la lista de índices a borrar
    baseHackeada.pop(i) #elimina el elemento de la base enviando su índice
print(baseHackeada)         #imprime la base sin los elementos borrados

#LITERAL C

faltantes = []
for usuarios in copiaOctubre: #recorre la copia
    encontrado = False
    for datos in baseHackeada1: #recorre la base
        if usuarios[0]==datos[3]: #compara si el usuario (pos 0) existe en la base (pos 3)
            encontrado = True
    if encontrado == False and datos not in faltantes:
        faltantes.append(usuarios)
print("Faltantes:",faltantes)