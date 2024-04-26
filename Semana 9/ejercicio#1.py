kilometros_por_dia = [0] * 7  

#Pide los km por dia
for dia in range(7):
    kilometros = float(input(f"Ingrese los kilómetros recorridos el día {dia + 1}: "))
    kilometros_por_dia[dia] = kilometros

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
total_semana = 0
#imprime los km por dia
for dia in range(7):
    print("Kilómetros recorridos el", dias_semana[dia] + ":", kilometros_por_dia[dia])
    total_semana += kilometros_por_dia[dia]

print("Total de la semana:", total_semana)
