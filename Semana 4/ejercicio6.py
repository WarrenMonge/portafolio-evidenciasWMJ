#Ejercicio 6

repuesto = input("Ingrese el tipo de repuesto (por ejemplo, 'motor', 'accesorios', 'limpieza', 'frenos'): ")


if repuesto.lower() == "motor":
    descuento = 0.15  
elif repuesto.lower() == "accesorios":
    descuento = 0.10 
elif repuesto.lower() == "limpieza":
    descuento = 0.05  
elif repuesto.lower() == "frenos":
    descuento = 0.03  
else:
    input("El tipo de repuesto ingresado es incorrecto!!!!!.")

precio = float(input("Ingrese el precio del repuesto: "))

monto_descuento = precio * descuento

precio_final = precio - monto_descuento

print("Descuento aplicado:", monto_descuento)
print("Precio final con descuento:", precio_final)
