
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