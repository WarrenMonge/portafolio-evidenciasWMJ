# Datos de ejemplo: tiempos de vuelta y tiempos de pits (en segundos)
tiempos_vuelta = [80, 78, 82, 79, 81, 83, 77, 80, 79, 82]
tiempos_pits = [20, 22, 18, 21, 19, 23, 20, 22, 21, 19]
# Cálculo del tiempo promedio por vuelta
tiempo_promedio_vuelta = sum(tiempos_vuelta) / len(tiempos_vuelta)
# Cálculo del tiempo promedio por PITS
tiempo_promedio_pits = sum(tiempos_pits) / len(tiempos_pits)
# Cálculo del porcentaje de tiempo de PITS respecto al tiempo de recorrido de una vuelta
porcentaje_pits_vs_vuelta = (sum(tiempos_pits) / sum(tiempos_vuelta)) * 100
# Resultados
print(f"Tiempo promedio por vuelta: {tiempo_promedio_vuelta:.2f} segundos")
print(f"Tiempo promedio por PITS: {tiempo_promedio_pits:.2f} segundos")
print(f"Porcentaje de tiempo en PITS respecto al tiempo de recorrido de una vuelta: {porcentaje_pits_vs_vuelta:.2f}%")
