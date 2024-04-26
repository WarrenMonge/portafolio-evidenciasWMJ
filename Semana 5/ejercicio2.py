print("2) Ejemplo 2")
c_aprobados = 0
c_desaprobados = 0
n_mayor = 0
n_menor = 100
c_total = 0


opc = input("Ingrese Y si quiere agregar nota de estudiante o N si quieres salir: ")
while opc == "y":
    nota = int(input("Ingrese la nota del estudiante: "))
    opc = input("Ingrese Y si quiere agregar nota de estudiante o N si quieres salir: ")
    if nota > n_mayor:
        n_mayor = nota
        
    if nota < n_menor:
        n_menor = nota

    if nota >= 70:
        c_aprobados = c_aprobados + 1
    else:
        c_desaprobados = c_desaprobados + 1

    c_total = c_total + 1

print("\n La cantidad total de estudiantes es de : ", c_total)
print("\n La nota mas alta es: ", n_mayor)
print("\n La nota mas baja es: ", n_menor)
print("\n La cantidad estudiantes reprobados es de : ", c_desaprobados)
print("\n La cantidad estudiantes aprobados es de : ", c_aprobados)



