#Tema 1
'''a = float("5,1")  #error no es un float, corregir a “5.1”
a2 = 6 * a > 30   #30.6>30
print("Está imprimiendo ", a2) #imprime True'''



#Tema 2
frase = "Todos Flotarán Al Final Del Semestre"
x = frase.find("al")+frase.count("a")
print("A: ", x)
x = frase[:len(frase)//2].count("s")
print("B: ", x)
x = frase[::-1].lower().istitle()
print("C: ", x)
x = frase[-10:].count("l")
print("D: ", x)
x = frase[:frase.find("Al")].split()
print("E: ", x)
x = frase.replace("Flotarán", "Aprobarán")
print("F: ", x)
x = x + "No, era una broma"
print("G: ", x)
x = frase.replace(" ", "").isalpha()
print("H: ", x)

#Tema 3
'''Devolverá True, siempre y cuando el Tweet empiece con una letra, finalice con un número,
contenga un url (http://), tenga una mención a la cuenta @espol y un hashtag #.
El tweet debe tener 140 caracteres o menos.'''

tweet = "En @espol se celebran los #59años, visita http://www.espol.edu.ec/eventos, ya casi 60"
validacion = tweet[0].isalnum() and tweet.count("http://")>0 \
             and tweet.find("@espol")!=-1 and tweet.count("#")>0 and len(tweet)<=140
print("Tweet: ", validacion)