from GestionUsuarios.Usuarios import Usuarios


class Administradores(Usuarios):
    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

    def desbloquearCiudadanos(self,Ciudadanos):
        pass

    def bloquearCiudadanos(self,Ciudadano):
        pass

    def administrarEventos(self,Evento):
        pass