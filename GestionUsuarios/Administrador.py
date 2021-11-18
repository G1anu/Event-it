from GestionUsuarios.Ciudadano import Ciudadano


class Administrador():

    def __init__(self, usuario, contrasena, accesoAABM):
        self.usuario = usuario
        self.contrasena = contrasena
        self.accesoAABM = accesoAABM

    def booleanNumericoAccesoAABM(self):
        if self.accesoAABM == True:
            return 1
        else:
            return 0

    def adminAEscribir(self):
        return [str(self.usuario),str(self.contrasena),self.booleanNumericoAccesoAABM()]


# pasarle un ciudadano y desbloquearlo
    def desbloquearCiudadano(self,Ciudadano):
        Ciudadano.estaBloqueado = False
        Ciudadano.solicitudesRechazadas = 0
        return ("El ciudadano se ha desbloqueado")

# pasarle un ciudadano y bloquearlo
    def bloquearCiudadano(self,Ciudadano):
        Ciudadano.estaBloqueado = True
        return("El ciudadano se ha bloqueado")

# los administradores puedan crear tipos de eventos
    def CrearTipoDeEvento(self,nuevoTipo):
        #esto va a tener que llamar a la persistencia para guardarse en una lista, como todavia no la hicimos no podemos avanzarlo
        pass
