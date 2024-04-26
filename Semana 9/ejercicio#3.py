palabra = input("Ingrese una palabra: ")

palabra_al_reves = ""

for i in range(len(palabra) - 1, -1, -1): # se itera de atras hacia adelante
    palabra_al_reves += palabra[i] # Se guarda la palabra en orden inverso

print("La palabra al revés es:", palabra_al_reves)