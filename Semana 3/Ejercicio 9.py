#EJERCICIO 9

horas= int(input("Dijite la cantidad de horas trabajadas: "))
minutos = int(input("Dijite la cantidad de minutos trabajados: "))
segundos = int(input("Dijite la cantidad de segundos trabajados: "))
segundos_totales = horas * 3600 + minutos * 60 + segundos

print("La cantidad de segundos totales trabajados es de: ", segundos_totales, "segundos")
