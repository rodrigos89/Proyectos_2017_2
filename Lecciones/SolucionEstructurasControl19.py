#1. Su programa debe preguntar cuantas fechas desea validar (lim)
#2. Los formatos aceptados pueden ser: dd-mm-aaaa o dd/mm/aaaa
#3. Los días pueden ser del 1 al 30
#4. Los meses solo pueden ser del 1 al 12
#5. El año debe contener 4 digitos, y ser mayores a 1900 y menores a 2018
#6. Cuando no sea válido el formato, día, mes o año, presentar un mensaje personalizado.
# Otro ejm: El formato xxxx no es válido. El día 34 no es válido.
#7. Mientras no se digite bien la fecha seguirá su programa pidiendo una fecha válida
#8. Cuando su programa finalice presente todas las fechas validadas (lista).

lim = int(input("Ingrese limite: "))
listaFechas = []
for i in range(lim):
    fechanoValida = True
    fecha = ""
    while fechanoValida:
        fecha = input("Ingrese fecha:")
        dia = int(fecha[:2])
        sep1 = fecha[2]
        mes = int(fecha[3:5])
        anio = int(fecha[-4:])
        sep2 = fecha[5]
        if len(fecha)== 10:
            if (sep1 == "-" and sep1 == sep2) or (sep1 == "/" and sep1 == sep2):
                if (0 < dia < 31):
                    if(0<mes<13):
                        if(1899<anio<2018):
                            fechanoValida = False
                            print("Fecha válida")
                            listaFechas.append(fecha)
                        else:
                            print("%d no es un año válido" % anio)
                    else:
                        print("%d no es un mes válido" % mes)
                else:
                    print("%d no es un día válido"%dia)
            else:
                print("%s no es un formato válido"%fecha)

print("Fechas validadas:", listaFechas)