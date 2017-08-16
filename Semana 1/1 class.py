num1 = 17
print(num1)
num2 = 2.5
print(num2)

cad1 = "UIP"
print(cad1)
cad2 = 'Panama'
print(cad2)
cad3 = """ Este es un ejemplo de una cadena de varias lineas... """
print(cad3)


s1 = True
s1 = False


#introduccion de datos
nombre = input("NOMBRE: ")
edad = int(input("EDAD: "))     #pedir por teclado


while True:
    print("BIENVENIDO, " + nombre + ". Tienes " + str(edad) + " años.")

    if (edad < 18):
        print("\nEstas castigado")
    elif (edad == 18):
        print("\nPuedes salir\t...\tPero ven temprano")
    else:
        print("\tLarga a trabajar!")

    salida = input("Desea continuar(S/N): ")
    if salida.upper () !="S" or salida !="s":
        break

print("Ciao!")