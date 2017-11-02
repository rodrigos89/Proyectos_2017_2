#Tema 1
a = float("5.1")
a2 = 6 * a > 30   #30.6>30
print("Está imprimiendo ", a2) #imprime True'''


#Tema 2
frase = "Todos Flotarán Al Final Del Semestre"
x = frase.find("al")
print("A: ", x)
x = frase[:len(frase)//3].count("a")
print("B: ", x)
x = frase[::-1].lower().istitle()
print("C: ", x)
x = frase[-10:].count("e")
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
'''Devolverá True, siempre y cuando el Tweet empiece con una letra o un número, contenga un
url (http://), tenga una mención a la cuenta @espol y más de un hashtag #.
El tweet debe tener 140 caracteres o menos.'''

tweet = "En @espol se celebran los #59 años, enterate de nuestros #eventos en http://www.espol.edu.ec/es/calendario-eventos"

validacion = tweet[0].isalnum() and tweet.count("http://")>0 \
             and tweet.find("@espol") and tweet.count("#")>1 and len(tweet)<=140
print("Tweet: ", validacion)