def imprimir_diccionario(w):
    print("\nMi lista de supermercado...")
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)


if __name__ == '__main__':
    diccionario = {}

    while True:
        print('\n\nLISTA DE SUPERMERCADO')
        print('1. Agregar elemento')
        print('2. Quitar elemento')
        print('3. Ver lista')
        print('4. Salir')
        try:
            opc = int(input("OPCION: "))
        except ValueError:
            opc = 0

        if opc == 1:
            print("\nElemento a ingresar")
            artInsertar = input("Articulo: ")
            if artInsertar not in diccionario:
                diccionario[artInsertar]
            else:
                diccionario[artInsertar] +=1
        elif opc == 2:
            print("Vamos a quitar un articulo de la lista...")
            artBorrar = input("Articulo: ")
            if artBorrar in lista:
                lista.remove(artBorrar)
            else:
                print("404 not found")
        elif opc == 3:
            imprimir_lista(lista)
        elif opc == 4:
            break
        else:
            print("ERROR: :Opcion no valida ")
    print("HASTA LUEGO!")