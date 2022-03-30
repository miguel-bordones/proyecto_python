def fibonacci(numero):
   if numero <= 2: print("La cantidad debe ser mayor a 2.")
   else:
      serie = [0,1]
      for i in range(numero-2):
         serie.append(serie[-1] + serie[-2])
      return serie
print(fibonacci(12))