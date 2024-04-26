def agregar_informacion(notas):
    with open(notas, 'a') as db:
        nombre = input("Ingrese el nombre del estudiante: ")
        grupo = input("Ingrese el grupo del estudiante: ")
        calificacion = input("Ingrese la calificación del estudiante: ")

        db.write(nombre + ',' + grupo + ',' + calificacion + '\n')

    print("Información agregada correctamente.")

def mostrar_informacion(notas):
    with open(notas, 'r') as db: #Modo lectura
        print("Nombre\tGrupo\tCalificación")
        for linea in db:
            nombre, grupo, calificacion = linea.strip().split(',')
            print(nombre + '\t' + grupo + '\t' + calificacion)

def menu():
    print("\n*** Menú ***")
    print("1. Agregar información de un estudiante")
    print("2. Mostrar información de todos los estudiantes")
    print("3. Salir")

notas = "Semana 11/notas.txt"

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_informacion(notas)
    elif opcion == '2':
        mostrar_informacion(notas)
    elif opcion == '3':
        print("Muchas gracias por usar el programa!!!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
