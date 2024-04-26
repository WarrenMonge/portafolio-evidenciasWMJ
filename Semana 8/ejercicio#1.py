def bin(decimal):
    print("DECIMAL A BINARIO")
    lista = []

    while (decimal >= 1):
        lista.append(decimal % 2)
        decimal = int(decimal / 2)

    s = lista[::-1]
    
    for k in s:
        print(k, end="")

def octal(decimal):
    print("\nDECIMAL A OCTAL")
    lista = []

    while (decimal >= 1):
        lista.append(decimal % 8)
        decimal = int(decimal / 8)

    s = lista[::-1]
    
    for k in s:
        print(k, end="")

def hex(decimal):
    print("\nDECIMAL A HEXADECIMAL")
    hexadecimales = ["0",
                     "1",
                     "2",
                     "3", 
                     "4", 
                     "5",
                     "6", 
                     "7", 
                     "8",
                     "9",
                     "A", 
                     "B", 
                     "C", 
                     "D", 
                     "E",
                     "F"]
    
    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16
        hexadecimal = hexadecimales[resto] + hexadecimal
        decimal = decimal // 16
    print(hexadecimal)

decimal = int(input("Ingrese el numero en decimal: "))

bin(decimal)
octal(decimal)
hex(decimal)