print("4) Ejemplo 4")
suma_pares = 0

for i in range(1, 11):
    valor = int(input(f"Ingrese el valor {i}: "))
    if valor % 2 == 0:
        suma_pares += valor


print("La suma de los números pares es:", suma_pares)