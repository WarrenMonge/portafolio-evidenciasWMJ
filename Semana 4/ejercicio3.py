#Ejercicio 3

anno = int(input("Ingrese su año de nacimiento: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print(anno, "es un año bisiesto.")
else:
    print(anno, "no es un año bisiesto.")