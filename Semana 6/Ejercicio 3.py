n = int(input("Ingrese un numero: "))

divisibles = []
contador = 1

while len(divisibles) < 10:
    if contador % n == 0:
        divisibles.append(contador)
    contador +=1

print(f"Los primeros 10 numeros divisibles entre {n} son: {divisibles}")
