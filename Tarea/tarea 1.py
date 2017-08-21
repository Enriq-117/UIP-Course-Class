# Tarea 1 - Programación 3
# Haga un programa que lea las ventas mensuales de todos los vendedores de la compañia ABC, muestre las ventas totales,
# el vendedor que mas vendio y el que menos vendio. Finalmente si ABC, paso la meta mensual, que es 1,000,000

print("\n======> COMPAÑÍA ABC <======")

def imprimir_diccionario(w):
    print("\nVENTAS")

    for art, cant in w.items():
        print("Venta\n: " + str(art))


if __name__ == '__main__':
    diccionario = {}

    while True:
        print('VENTAS')
        print('1. Añadir venta')
        print('2. Suma de ventas')
        print('3. Mostrar lista de la(s) venta(s) de la compañía')
        print('4. Salir')
        try:
            opc = int(input("\nOPCIÓN:"))
        except ValueError:
            opc = 0

        if opc == 1:
            print("\nDigitar venta")
            artInsertar = int(input("Venta: "))

            if artInsertar not in diccionario:

                 diccionario[artInsertar] = 1
            else:

                 diccionario[artInsertar] += 1
        elif opc == 2:
            menor = 9999999999999999999
            mayor = 0
            print("\nSuma de ventas")
            s = sum(diccionario.keys())
            print(s)

            if s > 1000000:

                print("En horabuena! ABC sobrepasó la meta mensual\n")
            else:

                print("\nLa compañia no pasó la menta, Busque la luz...\n")

        elif opc == 3:

            imprimir_diccionario(diccionario)

        elif opc == 4:

           break
        else:
            print("ERROR::Opcion inválida")
    print("See ya´ soon")