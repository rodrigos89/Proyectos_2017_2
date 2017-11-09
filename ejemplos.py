val = -15
i = 0
for i in range(val,-4,3):
    val+=5
print("i:",i)
print("val:",val)


val = -5
i = 0
for i in range(val,i):
    val+=i
print("i:",i)
print("val:",val)


#Escriba un programa que permita validar formatos de 2010-2050

#1. Su programa debe realizar la validación de 5 entradas
#2. Los formatos aceptados pueden ser: mm-dd-aa o mm-dd-aaaa
#3. Valide la longitud de la entrada
#4. Los días pueden ser del 01 al 28
#5. Los meses solo pueden ser del 01 al 12
#6. El año debe contener 4 digitos mayores a 2010 y menores a 2050
#7. Cuando no sea válido el día, mes o año, presentar un mensaje personalizado. Por ejm: El día 29 no es válido.
#   Otro ejm: El formato no es válido.
#8. Cuando su programa finalice mencione cuantas fechas ingresadas fueron válidas

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
                        else:
                            print("%d no es un año válido" % anio)
                    else:
                        print("%d no es un mes válido" % mes)
                else:
                    print("%d no es un día válido"%dia)
            else:
                print("%s no es un formato válido"%fecha)
    listaFechas.append(fecha)
