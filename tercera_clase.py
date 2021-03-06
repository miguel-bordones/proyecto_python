#Argumentos de longitud variable
""" def sumar(*args):
 print(type(args))
 print(args)
 total = 0
 for n in args:
   total += n
 return total
print(sumar(10,0,4,5,8,7,8)) """

""" def sumar(**kwargs):
   print(type(kwargs))
   print(kwargs)
   total = 0
   for n in kwargs:
      total += kwargs[n]
   print(total)
sumar(a=5, b=20, c=23) """

#Ejercicio Promedio variable
""" def promedio_variable(*numeros):
    #total = 0
    #for n in args:
        #total += n
    promedio = sum(numeros) / len(numeros)
    return promedio

print (promedio_variable(10,5,6,4)) """

#Fución de orden superior
""" def sumar100(num):
   return num + 100

def elevarCuadrado(num):
   return num**2

def superior(funcion, lista):
   resultado = []
   for n in lista:
      resultado.append(funcion(n))
   return resultado

print(superior(elevarCuadrado, [2,3,4]))
print(superior(lambda x: x**3, [2,3,4])) """

#Función map
""" resultado = list(map(lambda x: x**3, [2,3,4]))
print(resultado) """

#Manejo de excepciones
""" try:
   edad = int(input("Ingresá tu edad: "))
   #print(dsf)
except:
   print("Algo salió mal")
 """
""" except (ValueError, NameError):
   print("Algo salió mal

except ValueError:
   print("Esto no se puede castear a números")
except NameError:
   print("Hay un valor desconocido")  """

""" try:
 int("Hola")
except Exception:
 print("Ocurrió un error.")
else:
 print("Todo salió bien.")
finally:
 print("Final del bloque")
 """

""" def sumar(a, b):
 if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
   raise TypeError("Se requieren dos numeros.")
 return a + b

try:
   print(sumar('hola', 5)) 
except TypeError:
   print("Alguno no es número") """

#Ejercicio Calculadora
""" while True:
   try:
      a = float(input("Ingrese el primer número: "))
      b = float(input("Ingrese el segundo número: "))
      suma = a + b
      resta = a - b
      multiplicacion = a * b
      division = a / b
      print(suma, resta, multiplicacion, division)
      break
   except ValueError:
      print("Sólo se pueden ingresar números")
   except ZeroDivisionError:
         print ("No se puede dividir por 0")
 """

#Ejercicio países
# Diccionario código: país.
paises = {
 "ar": "Argentina",
 "es": "España",
 "us": "Estados Unidos",
 "fr": "Francia",
 "ve": "Venezuela"

}

while True:
   pais = input("Por favor ingresá el código de país ('salir' para salir): ")
   if pais == 'salir': break
   try:
      print("El país seleccionado es:", paises[pais])
   except KeyError:
      print("Este código de país no está en la lista")
