#EJERCICIO 1

def suma(num1, num2):
    suma = num1 + num2
    return suma

def resta(num1, num2):
    restar = num1 - num2
    return restar

def multi(num1, num2):
    multipli = num1 * num2
    return multipli

def division(num1, num2):
    divi = num1 / num2
    return divi

print("Bienvenido a la calculadora!!!!!!!")


operacion = input("""Ingrese la operacion que desea: 
        a) Suma
        b) Resta
        c) Multiplicacion
        d) Division
        s) Salir                  
        """)
parameter_a = int(input("INgrese el Primer numero: "))
parameter_b = int(input("INgrese el Segundo numero: "))
resultado_operacion = None
if operacion == "a":
    resultado_operacion = suma(parameter_a, parameter_b)
elif operacion == "b":
    resultado_operacion = resta(parameter_a, parameter_b)
elif operacion == "c":
    resultado_operacion = multi(parameter_a, parameter_b)
elif operacion == "d":
    resultado_operacion = division(parameter_a, parameter_b)
elif operacion == "s":
    input("Gracias por usar la calculadora!!!")
else:
    input("Ingresaste la operacion incorrecta!!!")

if resultado_operacion != None:
    input("El resultado es: ", resultado_operacion )