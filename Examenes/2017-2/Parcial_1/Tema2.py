#Procesar datos dentro de una cadena

listaIndicadores = ["INR", "RBC", "BGT", "ESR", "HGB", "TA", "WBC"]

resultado = "Resultado de Laboratorio ‘Su Salud’ Nombre del paciente: José Aimas " \
            "E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: " \
            "INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora " \
            "RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. " \
            "Los valores de este informe no representan un diagnóstico. " \
            "Firma médico responsable Dr. Juan Pozo Rodriguez"

'''resultado = "Resultado de Laboratorio 'Sana' Nombre del paciente: Ginger Irene Cruz" \
            "Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL " \
            "Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth " \
            "Plaza"'''

listaResultado = resultado.split() #Separando cada palabra de la cadena

nota = False
print("INFORME DE LABORATORIO".center(30," ")) #Impresión inicial encabezado
print("".center(30,"*")) #Repetición de 30 *
for indicador in listaIndicadores: #recorriendo la lista de indicadores
    if indicador in listaResultado: #busca el indicador en la lista de palabras
        pos = listaResultado.index(indicador) #Si está ya puede buscar el índice del mismo
        valor = listaResultado[pos+1] #el valor sería el siguiente elemento despues del indicador
        medida = listaResultado[pos+2] #la medida sería el siguiente elemento despues del valor
        if indicador == "HGB" and float(valor)<14: #para validar la hemoglobina
            print(indicador, "\t".join((valor.rjust(15, " "),medida.rjust(10," "),"**")))
            nota = True
        else:
            print(indicador.ljust(3," "), "\t".join((valor.rjust(15, " "),medida.rjust(10," "))))
posdoctor = "Dr." in listaResultado #busca si hay un Dr.
posdoctora = "Dra." in listaResultado #busca si hay una Dra.
if posdoctor: #si es Dr.
    posdr = listaResultado.index("Dr.") #busca su índice
if posdoctora: #si es Dra.
    posdr = listaResultado.index("Dra.") #busca su índice
if posdoctor or posdoctora: #si encontró alguno de los dos se intenta buscar los nombres
    nombre = " ".join(listaResultado[posdr+1:]) #el nombre está en los siguientes elementos
    print()
    print("Médico:",nombre)
if nota:
    print("** El valor de hemoglobina está por debajo de lo normal") #Si se cumplió lo de HGB