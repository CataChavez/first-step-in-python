#Esta línea es un comentario
print(1000) #Esto tambien es un comentario de una línea

"""Esto es 
un comentario
multilínea"""

print(round(1000 * 1.19)) #función round quita los decimales

#Cuando se calcula en python, hay que revisar la precedencia, se deben ocupar los parentesis.
print(round(12 + 10 * 2)) #En este caso dará 32

#Se deben ocupar los parentesis
print(round((12 + 10) * 2)) #En este caso dará 44
#orden de precedencia: raiz, multiplicación, división, suma, resta

#Reglas
#No se puede sumar strings con numeros.
#strings entre comillas simples o dobles.

#concatenación str
print("Esto es una concatencación" + " " + "con el operador ternario '+' ")
print("15" + "23") #esto resulta 1523
#duplicación
print(3 * "Carlos") #esto arroja CarlosCarlosCarlos
print(5 * "12") #esto arroja 1212121212

#Métodos

#count
#cuenta cuantas veces aparece un caracter específico en un sttring
print(("Esto es una concatencación" + " " + "con el operador ternario '+' ").count("a"))#Esto arroja que se repite 5 veces
print(("Esto es una concatencación" + " " + "con el operador ternario '+' ").count("o"))#Esto arroja que se repite 6 veces
print(("Esto es una concatencación" + " " + "con el operador ternario '+' ").count(""))#Esto arroja el numero de caracteres

#upper
#upper convierte todo a mayusculas solo visualmente
print("Esto es una concatencación".upper())#Esto arroja "ESTO ES UNA CONCATENACION"

#lower convierte todo a minusculas solo visualmente
print("ESTO ES UNA CONCATENCACIÓN".lower())#Esto arroja "esto es una concatencación"

#length
#contar el numero de caracteres en un string
print(len("Esto es una concatencación" + " " + "con el operador ternario '+' "))#Esto arroja el numero de caracteres, no conto el espacio

#Title .title()
#Join

#salto de línea \n  agrega un salto de línea dentro del string
print ("hola\na\ntodos")# arroja el string con los saltos indicados con el \n, arroja el string en 3 líneas.

#snakeCase
nombre_alumno = "Felipe Vera"
print(nombre_alumno)



