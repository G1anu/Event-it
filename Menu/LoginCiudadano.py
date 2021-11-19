from Anses.Anses import leerCuilsDelAnses
from Anses.Anses import leerDataEspecificaDeCiudadano
from Anses.Anses import escribirCiudadano
from Anses.Anses import leerDataEspecificaDeAdmin
from GestionUsuarios.Ciudadano import Ciudadano
from GestionUsuarios.Administrador import Administrador
from GestionUsuarios.ABM import crearAdministrador





def crearObjetoCiudadanoEnRuntime(cuilCiudadano,posicionDelCuil):
    ListaPosicionCiudadano = []
    leerDataEspecificaDeCiudadano(ListaPosicionCiudadano,cuilCiudadano)
    posicionCuilCiudadano = int(ListaPosicionCiudadano[posicionDelCuil])

    CiudadanoExiste = False
    if posicionCuilCiudadano == 1:
        CiudadanoExiste = True
    else:
        CiudadanoExiste = False
    Ciudadano












def EstaElUsernameCiudadano():
    cuilCiudadano=str(input("Ingrese su CUIL correspondiente, en caso de querer volver atras ingrese el numero 0: "))
    if cuilCiudadano == "0":
        login()
    else:
        ListaNombresDeCiudadano=[]
        leerDataEspecificaDeCiudadano(ListaNombresDeCiudadano,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelCuil = -1
        while indiceDeLista < len(ListaNombresDeCiudadano):
            if cuilCiudadano == ListaNombresDeCiudadano[indiceDeLista]:
                existeElUsuario = True
                posicionDelCuil = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeCiudadano)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            crearObjetoCiudadanoEnRuntime(cuilCiudadano,posicionDelCuil)
        else:
            print("Este CUIL no existe, escriba otro.")
            EstaElUsernameCiudadano()




















