#EJERCICIO 6

#Calcular el costo de viaje a la Universidad

#Solicito la distancia
distancia = int(input("Ingrese la distancia en kilómetros desde su casa hasta la Universidad: "))

#Solicito el costo por kilómetro y lo calculo}
costo_km = int(input("Ingrese el costo por kilómetro: "))
valor_km = costo_km * distancia
total = valor_km

#Solicitar la cantidad de dias que el usuario se presenta a la Universidad
cant_dias = int(input("Ingrese la cantidad de días que viaja a la Universidad: "))

costo_total = (total * 2) * 15

input("El costo total por cuatrimestre es de", costo_total," colones, viaja", cant_dias, "días/día por semana, la distancia desde su casa a la Universidad es de", distancia, "kilómetros y el costo por km recorrido es de", costo_km)

