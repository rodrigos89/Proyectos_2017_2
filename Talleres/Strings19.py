import os
import socket

ip = socket.gethostbyname(socket.gethostname())
usuario = socket.gethostname()

print("Sistema de Invitaciones Baile de Gala Par. 19".center(49, "*"))
print("Bienvenido %s!"%usuario)
print("\nIngrese datos de la persona que adquiere los boletos")

#Literal 1
matricula = input("Matrícula:")
print("Validación 1:", matricula.isdigit() and len(matricula)==9
      and int(matricula[0:4])>=2010 and int(matricula[0:4])<=2017)

nombres = input("Nombres completos:").title()
print("Validación 2:", nombres.count(" ")<3 and nombres.replace(" ", "").isalpha())

fechaNac = input("Fecha Nacimiento:")
print("Validación 3: ", len(fechaNac)==10 and 2017-int(fechaNac[-4:])>=18
      and fechaNac[2]=="-" and fechaNac[5]=="-" and fechaNac.replace("-","").isdigit())

sexo = input("Ingrese sexo:")
print("Validación 4:", sexo=="F" or sexo=="M")

correo = input("Correo ESPOL:").lower()
print("Validación 5: ", "espol.edu.ec" in correo)


#Literal 2
print("\nIngrese datos de la persona invitada")

matricula2 = input("Matrícula:")
print("Validación 1:", matricula2.isdigit() and len(matricula2)==9
      and int(matricula2[0:4])>=2010 and int(matricula2[0:4])<=2017 and matricula!=matricula2)

nombres2 = input("Nombres completos:").title()

print("Validación 2:", nombres2.count(" ")<3 and nombres2.replace(" ", "").isalpha())

fechaNac2 = input("Fecha Nacimiento:")
print("Validación 3: ", len(fechaNac2)==10 and 2017-int(fechaNac2[-4:])>=18
      and fechaNac2[2]=="-" and fechaNac2[5]=="-" and fechaNac2.replace("-","").isdigit())

sexo2 = input("Ingrese sexo:")
print("Validación 4:", sexo2=="F" or sexo2=="M")


correo2 = input("Correo ESPOL:").lower()
print("Validación 5: ", "espol.edu.ec" in correo)

#Literal 3
mensaje = "Estimada {0}, El sr. {1} le ha invitado " \
          "al 'Baile de Gala ESPOL' organizado por FEPOL el día 31 de octubre 2017. " \
          "\nPor favor, confirme su respuesta de invitación al correo {2}".format(nombres2,nombres,correo)

print()
print("Enviando correo...")
print()
print("De:", correo)
print("Para:", correo2)
print("Asunto: Invitación Baile de Gala")
#Literal 4
if (sexo=="M" and sexo2=="F"):
    print(mensaje)
elif(sexo=="F" and sexo2=="M"):
    print(mensaje.replace("Estimada","Estimado").replace("El sr", "La srita"))
elif(sexo=="M" and sexo2=="M"):
    print(mensaje.replace("Estimada", "Estimado"))
else:
    print(mensaje.replace("El sr","La srita"))