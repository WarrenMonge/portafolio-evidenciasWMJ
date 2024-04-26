#Ejercicio 5
retos_cumplidos = 0

for i in range(1, 6): 
    respuesta = input(f"¿Completó el reto {i}? (s/n): ")
    if respuesta.lower() == "s":
        retos_cumplidos += 1
    else:
        print("Realice de nuevo el reto", i)

if retos_cumplidos == 5:
    print("¡Siguiente Nivel!")
else:
    print("No completó todos los retos. Inténtelo nuevamente.")
