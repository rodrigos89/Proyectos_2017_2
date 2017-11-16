'''En ESPOL ha sucedido un gran problema el último fin de semana:
un hacker recientemente ha accedido a la base de datos de credenciales
de usuarios ESPOL y ha modificado las contraseñas de todos los usuarios.
Es por ello que, el profesor de Fundamentos de Programación Par 34
solicita a sus estudiantes resolver el problema suscitado. A pesar de todo
el caos que se vive en ESPOL, el Equipo de Tecnologías ha logrado recuperar
una copia del mes de agosto de la mayoría de matrículas y correos de usuarios ESPOL.
'''

baseHackeada = [[201023847, 'Carlos Agila', 'bot@espol.edu.ec', 'cagila', 1234],
                [201390384, 'Bot', 'correo@bot.ep', 'bot', 293848],
                [201123453, 'María Cedeño', 'mce@bot.edu.ec', 'mcedeno', 1234],
                [201323847, 'José Perez', 'jose@gmail.com', 'jperez', 2938],
                [201391928, 'Bot', 'correo@bot.ep', 'bot', 29393]]

copiaAgosto = [[201391927, 'pepe@espol.edu.ec'], [201123453, 'mcedeno@espol.edu.ec'],
                [ 201391921, 'rasarag@espol.edu.ec'], [201023847, 'cagil@espol.edu.ec'],
                [201391929, 'alex@espol.edu.ec'],[201323840, 'user@espol.edu.ec']]


'''Usando la copia del mes de octubre realizar las siguientes instrucciones:
a)	Crear una copia independiente de baseHackeada y actualizar los correos de las
matriculas que coincidan con copiaAgosto (5 ptos)
b)	Borrar los estudiantes de baseHackeada que no existan en copiaAgosto (5 ptos)
c)	Generar una lista de usuarios faltantes que consten en copiaAgosto y no en
la baseHakeada, con miras a conocer cuales también ha borrado el hacker. (2 ptos extra)
'''

#LITERAL A
#copia independiente
baseHackeada1 = baseHackeada.copy()

for usuarios in copiaAgosto: #recorre la copia
    for datos in baseHackeada1: #recorre la base
        if usuarios[0]==datos[0]: #compara si el usuario (pos 0) existe en la baseHack (pos 0)
            datos[2]=usuarios[1]    #si existe, se actualiza el correo (pos 2)
print("Actualizado:",baseHackeada1)            #imprime la base actualizada

#LITERAL B
listaborrar = []    #crea una lista para agregar todos los índices a borrar
for datos in baseHackeada:     #recorre la base hackeada
    encontrado=False           #para validar si no fue encontrado el usuario
    for usuarios in copiaAgosto:      #recorre la copia
        if datos[0] == usuarios[0]: #Si el usuario fue encontrado en algun elemnto de la copia cambia a True
            encontrado = True
    indice = baseHackeada.index(datos) #recupera el índice de la sublista
    if indice not in listaborrar and encontrado==False: #Si el indice aun no se agrega y no fue encontrado
        listaborrar.append(indice)                      #se agrega el índice

print("Elementos a borrar:",listaborrar)                #imprimiendo lista de índices a borrar

listaborrar.sort(reverse=True) #ordenando de mayor a menor, porque si primero se eliminan los menores,
                                # los mayores ya cambiarían de posición y no existe tal posición
for i in listaborrar: #recorre la lista de índices a borrar
    baseHackeada.pop(i) #elimina el elemento de la base enviando su índice
print("Luego de borrar:",baseHackeada)         #imprime la base sin los elementos borrados

#LITERAL C

faltantes = []
for usuarios in copiaAgosto: #recorre la copia
    encontrado = False
    for datos in baseHackeada1: #recorre la base
        if usuarios[0]==datos[0]: #compara si el usuario (pos 0) existe en la base (pos 3)
            encontrado = True
    if encontrado == False and datos not in faltantes:
        faltantes.append(usuarios)
print("Faltantes:",faltantes)