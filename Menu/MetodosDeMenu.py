from Anses.Anses import leerCuilsDelAnses
from Anses.Anses import leerDataEspecificaDeCiudadano
from Anses.Anses import escribirCiudadano
from Anses.Anses import leerDataEspecificaDeAdmin
from GestionUsuarios.Ciudadano import Ciudadano
from GestionUsuarios.Administrador import Administrador


def login():
    print("1- Registrarse")
    print("2- Iniciar sesion como administrador")
    print("3- Iniciar sesion como usuario")
    print("4- Salir del programa")
    x=int(input("seleccione la opción: "))  #hay que hacer una value exception acá
    if x==1:
        ContieneCuilEnAnses()
    elif x==2:
        EstaElUsernameAdmin()
    elif x==3:
        pass
    elif x==4:
        print("Gracias por usar el programa")
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
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + len(listaCUILsDelAnses)
            else:
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + 1
        if existeEnAnses == True:
            yaExisteElUsuario(cuil)
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
            posicionListaCuilDeUsersCreados = posicionListaCuilDeUsersCreados + len(listaCUILsDeUsersCreados)
        else:
            posicionListaCuilDeUsersCreados= posicionListaCuilDeUsersCreados + 1
    if estaDuplicado == True:
        print("El CUIL que ingresó es de un usuario ya creado. Si es el suyo vaya a login para iniciar sesión,sino escriba un nuevo cuil.")
        ContieneCuilEnAnses()
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
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + len(listaCelularesDeUsersCreados)
            else:
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + 1
        if estaDuplicado == True:
            print("El numero de telefono que ingresó se encuentra en uso por otro usuario, ingrese uno nuevo.")
            EstaRepetidoElCelular(cuil)
        else:
            creadorDelUsuario(cuil,celular)
    else:
        print("el numero ingresado no tiene 10 digitos,ingreselo otra vez.")
        EstaRepetidoElCelular(cuil)
def creadorDelUsuario(cuil,celular):
    intCUIL = int(cuil)
    intCelular = int(celular)
    CiudadanoACrear = Ciudadano(intCUIL,intCelular)
    escribirCiudadano(CiudadanoACrear)
    print("Se ha creado el usuario.")
    login()

def EstaElUsernameAdmin():
    username=str(input("Ingrese su nombre de usuario, en caso de querer volver atras ingrese el numero 0: "))
    if username == "0":
        login()
    else:
        ListaNombresDeAdmins=[]
        leerDataEspecificaDeAdmin(ListaNombresDeAdmins,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelNombre = -1
        while indiceDeLista < len(ListaNombresDeAdmins):
            if username == ListaNombresDeAdmins[indiceDeLista]:
                existeElUsuario = True
                posicionDelNombre = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeAdmins)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            EstaLaContrasenaAdmin(username,posicionDelNombre)
        else:
            print("Este username no existe, escriba otro.")
            EstaElUsernameAdmin()
def EstaLaContrasenaAdmin(username,posicionDelNombre):
    contrasena = str(input("Ingrese su contraseña, en caso de querer volver atras ingrese el numero 0: "))
    if contrasena == "0":
        login()
    else:
        ListaContrasenasAdmins=[]
        leerDataEspecificaDeAdmin(ListaContrasenasAdmins,1)
        if contrasena == ListaContrasenasAdmins[posicionDelNombre]:
            crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre)
        else:
            print("contraseña incorrecta, escribala de nuevo")
            EstaLaContrasenaAdmin(username,posicionDelNombre)
def crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre):
    ListaPosicionDelABM= []
    leerDataEspecificaDeAdmin(ListaPosicionDelABM,2)
    booleanABM = int(ListaPosicionDelABM[posicionDelNombre])
    ABM = False
    if booleanABM == 1:
        ABM = True
    else:
        ABM = False
    AdminEnRuntime = Administrador(username,contrasena,ABM)
    menuAdmin(AdminEnRuntime)
def menuAdmin(Admin):
    print("¿Que desea hacer?")
    print("1-Agregar tipo de evento")
    print("2-Bloquear usuario")
    print("3-Desbloquear usuario")
    print("4-Crear administrador")
    print("5-Modificar administrador")
    print("6-Eliminar administrador")