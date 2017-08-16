from App import Persona

if __name__== '__main__':
    print("BIENVENIDO")
    nombre = input("NOMBRE: ")
    edad = int(input("EDAD: "))
    p1 = Persona.Persona(nombre, edad)
    print(p1.es_mayor_edad())