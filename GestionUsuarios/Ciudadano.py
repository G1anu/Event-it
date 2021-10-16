


class Ciudadano():
    def __init__(self,CUIL,telefono):
        self.CUIL = CUIL
        self.telefono = telefono
        self.solicitudesRechazadas = 0
        self.estaBloqueado = False

    def booleanNumerico(self):
        if self.estaBloqueado == True:
            return 1
        else:
            return 0

    def ciudadanoString(self):
        return (str(self.CUIL) + "," + str(self.telefono) + "," + str(self.solicitudesRechazadas)+ "," + str(self.booleanNumerico()))

    def aceptarSolicitud(self):
        pass

    def rechazarSolicitud(self):
        pass

    def enviarSolicitud(self,ciudadano,evento):
        if self.estaBloqueado == True:
            return "Estas bloqueado, contactate con un administrador para ser desbloqueado."
        else:
            return Solicitud








