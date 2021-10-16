from datetime import  datetime
class Evento():
    def __init__(self,datetime,tipo_de_evento,cantidad_de_personas,cantidad_maxima_de_personas,localidad):
        self.fecha = datetime.datetime
        self.tipo_de_evento = tipo_de_evento
        self.cantidad_de_personas = cantidad_de_personas
        self.cantidad_maxima_de_personas = cantidad_maxima_de_personas
        self.localidad = localidad
        self.estaLleno = False

#creacion del evento con una localidad, fecha, tipo , cantidad de personas
    def crearEvento(self):
        pass

# imprimir por pantalla el evento creado o para guardar en Persistencia
    def eventoString(self):
        return (str(self.fecha) + "," + str(self.tipo_de_evento) + "," + str(self.cantidad_de_personas) + "," + str(self.cantidad_maxima_de_personas) + "," + str(self.localidad))

    def verificarSiEstaLleno(self):
        if (self.cantidad_de_personas >= self.cantidad_maxima_de_personas):
            self.estaLleno = True
            return ("Este evento está en su capacidad maxima")
        else:
            pass

    # devuelve la cantidad de personas
    def contabilizadorPersonas(self):
        return (self.cantidad_de_personas)
