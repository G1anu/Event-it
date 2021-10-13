from datetime import  datetime
class Evento():
    def __init__(self,datetime,tipo_de_evento,cantidad_de_personas,cantidad_maxima_de_personas,localidad):
        self.fecha = datetime.datetime
        self.tipo_de_evento = tipo_de_evento
        self.cantidad_de_personas = cantidad_de_personas
        self.cantidad_maxima_de_personas = cantidad_maxima_de_personas
        self.localidad = localidad

#creacion del evento con una localidad, fecha, tipo , cantidad de personas
    def crearEvento(self):
        pass

#
    def contabilizadorPersonas(self):
        return (self.cantidad_maxima_de_personas - self.cantidad_de_personas)
