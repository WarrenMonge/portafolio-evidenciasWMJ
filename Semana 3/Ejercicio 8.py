#EJERCICIO 8

producto = input("Dijite el producto que compro: ")
precio_produc = int(input("Dijite el valor del producto: "))
cantidad_produc = int(input("Dijite la cantidad de producto que compro: "))

iva = precio_produc * 0.13 * cantidad_produc

total = precio_produc * cantidad_produc

print("Nombre del producto: ", producto, "\nCantidad de compra de productos: ", cantidad_produc, "\nPrecio Unitario: ", precio_produc, "\nEl Total + IVA es de: ", total + iva)



