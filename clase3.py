print("********************************************************")
numeros_ganadores = []
for i in range (5):

    numero = int(input("Ingrese el numero ganador: "))
    numeros_ganadores.append(numero)

    numeros_ganadores.sort()
    print("*******************************************************")
    print("Los numeros ganadores son:", end = "")
    for numero in numeros_ganadores:
        print(numero, end=", ")