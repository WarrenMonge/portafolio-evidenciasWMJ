print("3) Ejemplo 3")
total_salarios = 0


for i in range(1, 11):
    salario = float(input(f"Ingrese el salario del colaborador {i}: "))
    salario_con_deduccion = salario * 0.9
    total_salarios += salario_con_deduccion

print("El total pagado por la empresa es", total_salarios)
