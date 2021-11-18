from GestionUsuarios import Administrador
from Anses.Anses import leerDataEspecificaDeAdmin,leerAdministradores,adminCleaner,adminListPlacerAfterClean

def crearAdministrador(nuevoUsuario, nuevaContrasena, accesoAABM):
    newAdmin = Administrador.Administrador(nuevoUsuario, nuevaContrasena, accesoAABM)
    return newAdmin

def eliminarAdministrador(usuarioAeliminar):
    listaNombres=[]
    leerDataEspecificaDeAdmin(listaNombres,0)
    indiceNombre = 0
    posicionDelNombre = -1
    while indiceNombre < len(listaNombres):
        if usuarioAeliminar == listaNombres[indiceNombre]:
            posicionDelNombre = indiceNombre
            indiceNombre = indiceNombre + len(listaNombres)
        else:
            indiceNombre = indiceNombre + 1
    listaAdmins = []
    leerAdministradores(listaAdmins)
    listaAdmins.pop(posicionDelNombre)
    adminCleaner()
    adminListPlacerAfterClean(listaAdmins)
    print("Se elimino el usuario " + usuarioAeliminar + ".")
# "Se le pasa un usuario de Administrador y se le modifica la contraseña y se guarda en el archivo de texto listaAdministradores"
def modificarAdministrador():
    pass