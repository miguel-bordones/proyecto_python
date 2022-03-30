#Estructuras de control
#clima = 'soleado'
"""if clima == 'lluvia':
   print("Me tomo el colectivo")
elif clima == 'nublado':
   print("Llevo paraguas")
else:
   print("Me voy caminando") """

#Operador Ternario
#print("Me tomo el colectivo" if clima == 'lluvia' else 'Me voy caminando')

""" a = 'Hola Mundo'
if a: print("La lista no está vacía.")
else: print("La lista está vacía.") """

#Estructuras de loop
#while
""" i = 0
while i < 5:
   print("Hola Mundo")
   i += 1 """

""" while True:
   print("Hola Mundo")
   break """

#for clásico
""" for i in range(10):
   print(i, "Hola Mundo") """

#for each
""" frase = "Hola Mundo"
for caracter in frase:
   #if caracter == 'M': break
   if caracter == 'u': continue
   print(caracter) """

""" x = 8
if x == 10:
   print("Ese es el valor")
else:
   pass """

#Ejercicio Sumatoria
""" lista = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for x in lista[:-1]:
    suma += x
for i in range(len(lista)-1):
   suma += lista[i]
print(suma) """

#Ejercicio Mostrar y eliminar
""" lalist = [1,2,3,4,5,6,7,8,9,10]
while lalist:
    print(lalist[0])
    del lalist[0]
    print(lalist) """

#Funciones
""" def imprimirTexto(nombre):
   print("Hola " + nombre)

imprimirTexto('Gonzalo') """
""" 
def sumar(a, b=9):
   '''num, num -> num
   Devuelve la suma de los dos números ingresados'''
   print(a)
   return a + b

resultado = sumar(b=2, a=6)
print(resultado)
help(sumar) """

#Ejercicio Sucesión de Fibonacci
""" def fibonacci(numero):
   if numero <= 2: print("La cantidad debe ser mayor a 2.")
   else:
      serie = [0, 1]
      for i in range(numero-2):
         serie.append(serie[-1] + serie[-2])
      return serie
print(fibonacci(10)) """

#Declaración de variables globales
c = 1
def sumar(a):
   global b
   b = 2
   return a + c + b

print(sumar(4), c, b+2)