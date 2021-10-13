from GestionUsuarios import Administradores
class ABM():
    def __init__(self,Usuario,Contraseña):
        self.Usuario = Usuario
        self.Contraseña = Contraseña



# "la idea es crear un administrador por consola y que se guarde en el archivo de texto => ListaAdministradores"
    def crearAdministradores(self):
        with open("ListaAdministradores.txt", 'W') as listaAdministradores:
            listaAdministradores.write(Administradores.Administradores(input("Elija usuario:"),Administradores.Administradores(input("Elija contraseña"))))


# " el objetivo es pasarle un usuario escrito por consola y que lo borre del archivo de texto ListaAdministradores"

    def eliminarAdministradores(self):
        with open("ListaAdministradores.txt",'r') as listaAdministradores:
            if(Administradores.Administradores.getUsuario() == input("Usuario buscado:")):
                del listaAdministradores(Administradores.Administradores.getUsuario()) # Se borraria el Administrador buscado con el Usuario

 # "Se le pasa un usuario de Administrador y se le modifica la contraseña y se guarda en el archivo de texto listaAdministradores"

    def modificarAdministradores(self):
        pass
