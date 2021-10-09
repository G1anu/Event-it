from GestionUsuarios.Usuarios import Usuarios


class Ciudadanos(Usuarios):
    def __init__(self,CUIL,telefono):
        self.CUIL = CUIL
        self.telefono = telefono


    def aceptarSolicitud(self):
        pass

    def rechazarSolicitud(self):
        pass

    def enviarSolicitud(self):
        pass






