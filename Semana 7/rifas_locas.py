#Estudio de caso

aporte_premio = { 500: "Hamburguesa con papas y gaseosa.",  
                 1000: "Cupon cena para 2 personas.",
                 2000: "Un día en el parque de diversiones con transporte y comida pago para 3 personas.",
                 5000: "Fin de semana todo incluido en hotel paradisiaco para 2 personas."
                 }


m_total_reca = 0

for semana in range(1,5):
    print("Semana", semana)

    n_ganador = int(input("Ingrese el numero ganador entre (1 - 100): "))
    m_semana = 0

    for i in range(1,101):
        name =  input("Dijite su nombre: ")
        cedula = int(input("Dijite su numero de cedula: "))
        monto = int(input("Ingrese el monto que aporto(500, 1000, 2000, 5000):"))

        if i == n_ganador:
            name_winner = name
            cedula_winner = cedula
            premio_winner = aporte_premio[monto]
        
        m_semana += monto
    
    print("\nGanador de la semana ", semana)
    print("Nombre:", name_winner)
    print("Cédula:", cedula_winner)
    print("Premio que obtuvo gracias a su aporte de :",premio_winner)
    print("En esta semana se recaudo un total de:", m_semana, "\n")
    m_total_reca += m_semana

print("En todas la semanas se recaudo un total de = ", m_total_reca)
input()