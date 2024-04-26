import os
os.system('cls')
opc = int(input("""Ventas de Fide
    
    1 - Agregar Ventas
    2 - Mostrar Ventas
            
Pulse cualquier tecla para salir!!!
            """))


if opc == 1:
    os.system('cls')
    opc_ventas = input("Deseas agregar uan venta? S / N ")
    while opc_ventas.upper() == "S":
        
        db = open("ventas.txt", "a+")

        nombre_vendedor = input("Ingrese nombre vendedor: ")
        monto_venta = input("Ingrese el monto de venta: ")

        db.write(nombre_vendedor)
        db.write(" ")
        db.write(monto_venta)
        db.write("\n")

        db.close()
        opc_ventas = input("Deseas agregar uan venta? S / N ")

elif opc == 2:
    os.system('cls')
    db = open("ventas.txt", "r")
    datos = db.read()
    print(datos)
    input()
    db.close()
else:
    input("Gracias por utilizar el programa de ventas de FIDE")