from datetime import  datetime
class Evento():
    def __init__(self,datetime,tipo_de_evento,cantidad_de_personas,cantidad_maxima_de_personas,vectorX,vectorY):
        self.fecha = datetime.datetime
        self.tipo_de_evento = tipo_de_evento
        self.cantidad_de_personas = cantidad_de_personas
        self.cantidad_maxima_de_personas = cantidad_maxima_de_personas
        self.estaLleno = False
        self.x = vectorX
        self.y = vectorY

    def booleanNumericoEstaLleno(self):
        if self.estaLleno == True:
            return 1
        else:
            return 0
# imprimir por pantalla el evento creado o para guardar en Persistencia
    def eventoAEscribir(self):
        return [str(self.fecha),str(self.tipo_de_evento),str(self.cantidad_de_personas),str(self.cantidad_maxima_de_personas),str(self.booleanNumericoEstaLleno()),str(self.x),str(self.y)]

    def verificarSiEstaLleno(self):
        if(self.cantidad_de_personas >= self.cantidad_maxima_de_personas):
            self.estaLleno == True
            return ("Este evento está en su capacidad maxima")
        else:
            pass

# devuelve la cantidad de personas
    def contabilizadorPersonas(self):
        return self.cantidad_de_personas