fila_teatro = [""] * 10  #Se crea lista para las 10 butacas

for butaca in range(10):  # Iterar sobre cada butaca
    nombre = input("Ingrese el nombre de la persona: ")
    posicion = int(input("Ingrese el número de butaca (1-10): "))
    

    if 1 <= posicion <= 10:

        fila_teatro[posicion - 1] = nombre
    else:
        print("El número de butaca ingresado no es válido. Debe estar entre 1 y 10.")

for i, nombre in enumerate(fila_teatro):
    if nombre:
        print("Butaca", i + 1, ":", nombre)
    else:
        print("Butaca", i + 1, ": Vacía")
