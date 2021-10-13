import datetime


class Solicitud():
    def __init__(self,CUILSender,CUILReceiver, evento):
        self.CUILSender = CUILSender
        self.CUILReceiver = CUILReceiver
        self.evento = evento
        self.fecha = datetime.datetime

