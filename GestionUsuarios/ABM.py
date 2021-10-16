from GestionUsuarios import Administrador
class ABM():

    def crearAdministrador(self,nuevoUsuario, nuevaContraseña,accesoAABM):
        newAdmin = Administrador(nuevoUsuario,nuevaContraseña,accesoAABM)
        return newAdmin

    def eliminarAdministrador(self):
     #esto va a tener que llamar a la persistencia para eliminar de la lista de admins, como todavia no la hicimos no podemos avanzarlo
        pass
 # "Se le pasa un usuario de Administrador y se le modifica la contraseña y se guarda en el archivo de texto listaAdministradores"

    def modificarAdministrador(self):
        pass