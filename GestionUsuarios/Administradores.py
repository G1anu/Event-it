from GestionUsuarios.Usuarios import Usuarios


class Administradores():

    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña


    def getUsuario(self):
        return self.usuario

    def getContraseña(self):
        return self.contraseña

# pasarle un ciudadano y desbloquearlo
    def desbloquearCiudadanos(self,Ciudadanos):
        pass
# pasarle un ciudadano y bloquearlo
    def bloquearCiudadanos(self,Ciudadano):
        pass
# los ciudadanos puedan crear eventos
    def administrarEventos(self,Evento):
        pass