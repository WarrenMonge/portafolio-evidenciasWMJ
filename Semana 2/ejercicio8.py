#EJERCICIO 8
 
#Calcular salario mensual del usuario y aplicar rebajas

#Solicito la cantidad de horas trabajadas mensualmente
horas_sem = int(input("Ingrese la cantidad de horas trabajadas semanalmente: "))

#Solicito el precio de la hora
precio_hora = int(input("Ingrese el valor de la hora: "))

#Calculo el salario semanal
sal_semanal = horas_sem * precio_hora 

#Calculo el salario mensual
sal_mensual = sal_semanal * 4.2 - 0.105 - 0.05

print("El salario mensual del usuario es de", sal_mensual, "colones, y el semanal es", sal_semanal, "colones")
