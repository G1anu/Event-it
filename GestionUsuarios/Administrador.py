from Ciudadano import Ciudadano


class Administrador():

    def __init__(self, usuario, contraseña, accesoAABM):
        self.usuario = usuario
        self.contraseña = contraseña
        self.accesoAABM = accesoAABM


    def getUsuario(self):
        return self.usuario

    def getContraseña(self):
        return self.contraseña

# pasarle un ciudadano y desbloquearlo
    def desbloquearCiudadanos(self,Ciudadano):
        Ciudadano.estaBloqueado = False
        Ciudadano.solicitudesRechazadas = 0
        return ("el ciudadano se ha desbloqueado")

# pasarle un ciudadano y bloquearlo
    def bloquearCiudadanos(self,Ciudadano):
        Ciudadano.estaBloqueado = True
        return("el ciudadano se ha bloqueado")


# los administradores puedan crear tipos de eventos
    def administrarEventos(self,Evento):
        return Evento.tipo_de_evento()
