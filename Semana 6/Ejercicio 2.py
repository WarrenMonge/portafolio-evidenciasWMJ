#Ejercicio 2

h_1 = 0 #menos de 100 cm.
h_2 = 0 #entre 100 y 120 cm.
h_3 = 0 #entre 121 y 130 cm.
h_4 = 0 #entre 131 y 140 cm.
h_5 = 0 #más de 140 cm.
suma_altura = 0

n_ninos = int(input("Ingrese la cantidad de ninos que va a registrar la estatura: "))

for i in range(n_ninos):
    h = int(input("Ingrese la estatura del nino: "))
    if h < 100:
        h_1 += 1
    elif h >= 100 and h <=  120:
        h_2 += 1
    elif h >= 121 and h <=  130:
        h_3+= 1
    elif h >= 131 and h <=  140:
        h_4 += 1
    elif h > 140:
        h_5 += 1
    suma_altura += h
prom = suma_altura / n_ninos
print("El promedio de estaturas es de: ", prom)
print("Cantidad de niños que miden menos de 100 cm: ", h_1,
      "\nCantidad de niños que miden entre 100 y 120 cm: ", h_2,
      "\nCantidad de niños que miden entre 121 y 130 cm: ", h_3,
      "\nCantidad de niños que miden entre 131 y 140 cm: ", h_4,
      "\nCantidad de niños que miden más de 140 cm: ", h_5)
