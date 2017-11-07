#Valida si la cadena tiene @, letras, números, guión

id = "rasarag@3-1"
acumulador = 0
for i in id:
    if(i.isalpha()):
        contA=1
    elif (i.isdigit()):
        contD = 1
    elif (i=="@"):
        contE = 1
    elif (i=="-"):
        contG=1

if contD==1 and contA == 1 and contD==1 and contG == 1:
    print("El usuario tiene letras, números, arroba y guión")