import GestionEventos.Evento
from GestionEventos.Solicitud import Solicitud


class Ciudadano():
    def __init__(self,CUIL,telefono):
        self.CUIL = CUIL
        self.telefono = telefono
        self.solicitudesRechazadas = 0
        self.estaBloqueado = False

    def booleanNumericoEstaBloqueado(self):
        if self.estaBloqueado == True:
            return 1
        else:
            return 0

    def crearEvento(self,newDate,tipo_de_evento,cantidad_de_personas,cantidad_maxima_de_personas,localidad):
        newEvento = GestionEventos.Evento(newDate,tipo_de_evento,cantidad_de_personas,cantidad_maxima_de_personas,localidad)
        return newEvento

    def ciudadanoString(self):
        return (str(self.CUIL) + "," + str(self.telefono) + "," + str(self.solicitudesRechazadas)+ "," + str(self.booleanNumericoEstaBloqueado()))

    def aceptarSolicitud(self):
        pass

    def rechazarSolicitud(self):
        pass

    def enviarSolicitud(self, Ciudadano, CUILAEnviar, evento):
        if self.estaBloqueado == True:
            return "Estas bloqueado, contactate con un administrador para ser desbloqueado."
        elif evento.estaLleno == True:
            return "el evento no tiene mas capacidad disponible"
        else:
            CuilSender = Ciudadano.CUIL
            newSolicitud = Solicitud(CuilSender, CUILAEnviar, evento)
            return newSolicitud