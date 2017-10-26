import os
import socket

ip = socket.gethostbyname(socket.gethostname())
usuario = socket.gethostname()

print("Sistema de Invitaciones Baile de Gala".center(49, "*"))
print("Bienvenido %s!"%usuario)
print("\nIngrese datos de la persona que adquiere los boletos")

#Literal 1
matricula = input("Matrícula:")
print("Validación 1:", matricula.isdigit() and len(matricula)==9
      and int(matricula[0:4])>=2008 and int(matricula[0:4])<=2017)

nombres = input("Nombres completos:").title()
print("Validación 2:", nombres.count(" ")<3 and nombres.replace(" ", "").isalpha())

fechaNac = input("Fecha Nacimiento:")
print("Validación 3: ", len(fechaNac)==10 and fechaNac.replace("-","").isdigit() and 2017-int(fechaNac[-4:])>=18
      and fechaNac[2]=="-" and fechaNac[5]=="-")

correo = input("Correo NO ESPOL:").lower()
print("Validación 4: ", "espol.edu.ec" not in correo)


#Literal 2
print("\nIngrese datos de la persona invitada")

matricula2 = input("Matrícula:")
print("Validación 1:", matricula2.isdigit() and len(matricula2)==9
      and int(matricula2[0:4])>=2008 and int(matricula2[0:4])<=2017 and matricula!=matricula2)

nombres2 = input("Nombres completos:").title()

print("Validación 2:", nombres2.count(" ")<3 and nombres2.replace(" ", "").isalpha())

fechaNac2 = input("Fecha Nacimiento:")
print("Validación 3: ", len(fechaNac2)==10 and fechaNac2.replace("-","").isdigit() and 2017-int(fechaNac2[-4:])>=18
      and fechaNac2[2]=="-" and fechaNac2[5]=="-")

correo2 = input("Correo NO ESPOL:").lower()
print("Validación 4: ", "espol.edu.ec" not in correo)

#Literal 3
mensaje = "Estimada {0}, El sr. {1} le ha invitado " \
          "al 'Baile de Gala ESPOL' organizado por FEPOL el día 31 de octubre 2017. " \
          "Por favor, confirme su respuesta de invitación al correo {3}".format(nombres2,nombres,correo)
print(mensaje)

