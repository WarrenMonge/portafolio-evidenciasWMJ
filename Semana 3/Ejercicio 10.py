#EJERCICIO 10

name = input("Dijite su nombre completo: ")
cedula = input("Dijite su numero de cedula: ")
salario_bruto = int(input("Dijite su salario en bruto: "))


ccss = salario_bruto * 0.08
ban_po = salario_bruto * 0.01
deducciones = ccss + ban_po 
sal_neto = salario_bruto - deducciones
 


print("Empleado: ", name, "\nIdentificacion: ", cedula,
      "\nSalario bruto: ", salario_bruto, "\nCCSS (8%): " , ccss,
      "\nBanco Popular: ", ban_po, "\nTotal deducciones: ", deducciones,
      "\nSalario neto: ", sal_neto)
      


