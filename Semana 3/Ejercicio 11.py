#EJERCICIO 11

name_produc = input("Dijite el nombre de producto: ")

price_sanjose = int(input("Dijite el precio en San Jose: "))
price_heredia = int(input("Dijite el precio en Heredia:"))
price_alajuela = int(input("Dijite el precio en Alajuela:"))


prom = (price_sanjose + price_heredia + price_alajuela) / 3
prom = int(prom)

print("El promedio de precio es de: ", prom)
