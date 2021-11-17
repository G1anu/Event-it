from Anses.Anses import leerCuilsDelAnses
from Anses.Anses import leerDataEspecificaDeCiudadano


def login():
    print("1- Registrarse")
    print("2- Iniciar sesion como administrador")
    print("3- Iniciar sesion como usuario")
    print("4- Salir del programa")
    x=int(input("seleccione la opción: "))  #hay que hacer una value exception acá
    if x==1:
        ContieneCuilEnAnses()
def ContieneCuilEnAnses():
    cuil = str(input("Ingrese su numero de CUIL sin guion(debe ser de 11 digitos, EJ: 23440529259), en caso de querer volver atras ingrese el numero 0: "))
    if cuil == "0":
        login()
    else:
        listaCUILsDelAnses = []
        leerCuilsDelAnses(listaCUILsDelAnses)
        posicionListaCuilsDelAnses = 0
        existeEnAnses = False
        while posicionListaCuilsDelAnses < len(listaCUILsDelAnses):
            if cuil == listaCUILsDelAnses[posicionListaCuilsDelAnses]:
                existeEnAnses = True
            else:
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + 1
        if existeEnAnses == True:
            yaExisteElUsuario()
        else:
            print("Su numero de Cuil no se encuentra en la lista del Anses, vuelva a escribirlo. En caso de seguir teniendo este problema comuniquese con el Anses.")
            ContieneCuilEnAnses()
def yaExisteElUsuario(cuil):
    listaCUILsDeUsersCreados = []
    leerDataEspecificaDeCiudadano(listaCUILsDeUsersCreados,0)
    estaDuplicado = False
    posicionListaCuilDeUsersCreados = 0
    while posicionListaCuilDeUsersCreados < len(listaCUILsDeUsersCreados):
        if cuil == listaCUILsDeUsersCreados[posicionListaCuilDeUsersCreados]:
            estaDuplicado = True
        else:
            posicionListaCuilDeUsersCreados= posicionListaCuilDeUsersCreados + 1
    if estaDuplicado == True:
        print("El CUIL que ingresó es de un usuario ya creado. Si es el suyo vaya a login para iniciar sesión,sino escriba un nuevo cuil")
        login()
    else:
        EstaRepetidoElCelular(cuil)
def EstaRepetidoElCelular(cuil):
    celular = str(input("Ingrese su numero de telefono sin su codigo de país(debe tener 10 digitos en total, EJ: 1154885993), en caso de querer volver atras ingrese el numero 0: "))
    if celular == "0":
        login()
    elif len(celular) == 10:
        listaCelularesDeUsersCreados = []
        leerDataEspecificaDeCiudadano(listaCelularesDeUsersCreados,1)
        estaDuplicado = False
        posicionListaCelularesDeUsersCreados = 0
        while posicionListaCelularesDeUsersCreados < len(listaCelularesDeUsersCreados):
            if celular == listaCelularesDeUsersCreados[posicionListaCelularesDeUsersCreados]:
                estaDuplicado = True
            else:
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + 1
        if estaDuplicado == True:
            print("El numero de telefono que ingresó se encuentra en uso por otro usuario, ingrese uno nuevo.")
            EstaRepetidoElCelular()
        else:
            pass
    else:
        pass

