#Consignas
# #Iniciar sesion como admin
#Iniciar sesion como usuario
#Registrarse (Crear usuario)
#Volver atras (Salir)




def login():
    while True:
        try:
            print("1- Registrarse")
            print("2- Iniciar sesion como administrador")
            print("3- Iniciar sesion como usuario")
            print("4- Salir del programa")

            x = int(input("Escriba el numero de la opción seleccionada: "))
        except ValueError:
            print("Introduzca un caracter válido")
