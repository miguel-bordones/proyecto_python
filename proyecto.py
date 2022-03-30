#Ejercicio Proyecto
# Hamburgueseria
pedido = 0
opcion = 0
resto = 0

empleados = {
 "1": "Juan",
 "2": "Gerardo",
 "3": "Miguel Bordones"
}

precios = {
 "c1": "5",
 "c2": "6",
 "c3": "7",
 "c4": "2"
}

#def menu(pedido):
 
print("Bienvenido a Hamburguesas IT")
emp = input ("Ingrese su nombre encargad@: ")
print("Bienvenido a Hamburguesas IT")
print("Encargad@ -> ", empleados[emp])
print("Recuerda, siempre hay que recibir al ")
print("cliente con una sonrisa :") 

   

print("1 - Ingreso nuevo pedido   ")
print("2 -  Cambio de turno")
print("3 - Apagar sistema")
###pedido = input("Opcion ", opcion)

if pedido == 1:
  while True:
    if confirma == 's' : break
    try:
        cliente = input ("Ingrese nombre del cliente: ")
        combo1 = input ("Ingrese cantidad Combo S : ")
        combo2  = input ("Ingrese cantidad Combo D: ")
        cantidadc = input("Ingrese cantidad Combo T: ")
        cantidadf = input("Ingrese cantidad Flurby: ")
        combo1 = combo1 * precios[c1]
        combo2 = combo2 * precios[c1]
        combo3 = combo3 * precios[c1]
        combo4 = combo4 * precios[c1]
        total = combo1 + combo2 + combo3 + combo4

        total =  input("Total ")
        abono = input("Abona con ")
        vuelto = abono - total

        print("Vuelto ", vuelto)

        pedido = input("¿Confirma pedido? Y/N : ")
    except KeyError:
       print("Error ")

#elif pedido == 2:

   
  


  
     
 