#EJERCICIO 9

#Solicitar ingresos mensuales
ing_mensuales = int(input("Ingrese sus ingresos mensuales: "))

#Solicitar gastos mensuales en alimentacion
gastos_alimentacion = int(input("Ingrese sus gastos mensuales en alimentacion: "))

porcentaje_alimentacion = (gastos_alimentacion * ing_mensuales)/100

porcentaje_otros = (porcentaje_alimentacion * ing_mensuales)/100

print("El porcentaje de gastos del rubro de alimentación es de ", porcentaje_alimentacion, "% y el porcentaje que queda disponible para otros rubros es de",porcentaje_otros,"%")



