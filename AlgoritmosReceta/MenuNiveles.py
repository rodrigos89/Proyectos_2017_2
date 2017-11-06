print("Bienvenido a mi Programa")
opcion = 0
while opcion!=5:
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Salir")
    opcion = int(input("Escoja una opción: "))
    if(opcion==1):
        print("Submenú 1")
        opcion = 0
        while opcion!=3:
            print("1. Escoja submenú 1")
            print("2. Escoja submenú 2")
            print("3. Salir")
            opcion = int(input("Escoja una opción: "))
            if(opcion==1):
                print("Ha seleccionado el submenú 1.")
            elif (opcion == 2):
                print("Ha seleccionado el submenú 2.")
            else:
                print("Saliendo de la opción 1.")
    elif (opcion == 2):
        opcion=0
        print("Submenú 2")
        while opcion != 4:
            print("1. Escoja submenú 1")
            print("2. Escoja submenú 2")
            print("3. Escoja submenú 3")
            print("4. Salir")
            opcion = int(input("Escoja una opción: "))
            if (opcion == 1):
                print("Ha seleccionado el submenú 1.")
            elif (opcion == 2):
                print("Ha seleccionado el submenú 2.")
            elif (opcion == 3):
                print("Ha seleccionado el submenú 3.")
            elif (opcion==4):
                print("Saliendo de la opción 2.")
            else:
                print("No ha seleccionado opción válida")
    elif (opcion == 3):
        opcion=0
        print("Submenú 3")
        while opcion != 2:
            print("1. Escoja submenú 1")
            print("2. Salir")
            opcion = int(input("Escoja una opción: "))
            if (opcion == 1):
                print("Ha seleccionado el submenú 1.")
            elif (opcion == 2):
                print("Saliendo de la opción 3.")
            else:
                print("No ha ingresado una opción válida.")
    elif (opcion == 4):
        print("Submenú 4")
        while opcion != 3:
            print("1. Escoja submenú 1")
            print("2. Escoja submenú 2")
            print("3. Salir")
            opcion = int(input("Escoja una opción: "))
            if (opcion == 1):
                print("Ha seleccionado el submenú 1.")
            elif (opcion == 2):
                print("Ha seleccionado el submenú 2.")
            elif (opcion == 3):
                print("Saliendo de la opción 4.")
            else:
                print("No ha ingresado una opción válida.")
    elif (opcion==5):
        print("Saliendo del programa.")
    else:
        print("Ha ingresado una opción no válida")