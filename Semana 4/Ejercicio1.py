#EJERCICIO 1

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))
num4 = int(input("Digite el cuarto numero: "))


if num1 > num2 and num1 > num3 and num1 > num4:
    print("El numero mas alto es: ",num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("El numero mas alto es: ",num2)
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("El numero mas alto es: ",num3)
else:
    print("El numero mas alto es: ",num4)
    
