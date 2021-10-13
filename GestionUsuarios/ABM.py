from GestionUsuarios import Administrador
class ABM():

    def crearAdministrador(self):
        with open("ListaAdministradores.txt", 'W') as listaAdministradores:
            listaAdministradores.write(Administrador.Administrador(input("Elija usuario:"), Administrador.Administrador(input("Elija contraseña"))))


# " el objetivo es pasarle un usuario escrito por consola y que lo borre del archivo de texto ListaAdministradores"

    def eliminarAdministrador(self):
        with open("ListaAdministradores.txt",'r') as listaAdministradores:
            if(Administrador.Administradores.getUsuario() == input("Usuario buscado:")):
                del listaAdministrador(Administrador.Administradores.getUsuario()) # Se borraria el Administrador buscado con el Usuario

 # "Se le pasa un usuario de Administrador y se le modifica la contraseña y se guarda en el archivo de texto listaAdministradores"

    def modificarAdministrador(self):
        pass
