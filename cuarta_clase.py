#Métodos de string
#strip
""" frase = "Hola Mundo"
frase = frase.strip('o')
print(frase) """

#replace
""" frase = "¡Nuestro gato se llamaba Indiana!"
frase = frase.replace('gato', 'perro')
print(frase) """

#split
#frase = "¡Nuestro gato se llamaba Indiana!"
""" archivo = "Jorge Ramírez,36254123,jorge@nada.com"
lista = archivo.split(',')
print(lista[1]) """

#Concatenar strings
""" nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
print("Hola " + nombre + ", y tu edad es " + str(edad) + ' años')
print(f"Hola {nombre}, y tu edad es {edad} años") """

#Ejercicio Mayúsculas
""" def convertir(lista):
   nueva_lista = []
   for elemento in lista:
      elemento = elemento.title()
      nueva_lista.append(elemento)
   return nueva_lista """

#nombres = ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]
#nueva_lista = list(map(lambda x: x.title(), nombres))
#nueva_lista = convertir(nombres)
#print(nueva_lista)

#Manejo de archivos
#archivo = open(r'C:\Users\gonza\Desktop\PP\fuentes\archivo.txt', 'r', encoding='utf-8')
#print(archivo.read())
#print(archivo.readlines())
""" for linea in archivo:
   linea = linea.strip()
   print(linea)
archivo.close() """

""" archivo_salida = open('fuentes/archivo_salida.txt', 'w', encoding='utf-8')
archivo_salida.write("Este es un archivo de texto de muestra\n")
archivo_salida.write("para que veamos como trabajar con\n")
archivo_salida.write("archivos con Python, con intención.\n")
archivo_salida.close() """

""" with open('fuentes/archivo_salida.txt', 'w', encoding='utf-8') as archivo_salida:
   archivo_salida.write("Este es un archivo de texto de muestra\n")
   archivo_salida.write("para que veamos como trabajar con\n")
   archivo_salida.write("archivos con Python, con intención.\n") """

""" hospitales = open('fuentes/hospitales.csv', encoding='utf-8')
lista_hospitales = []
for hospital in hospitales:
   hospital = hospital.strip()
   lista = hospital.split(',')
   lista_hospitales.append(lista[3])
   print(lista[3])
print(lista_hospitales) """

#import math
from math import sqrt as raizcuadrada
#print(sqrt(9))
print(raizcuadrada(9))
