import datetime


class Solicitud():
    def __init__(self,CUILSender,CUILReceiver, evento):
        self.CUILSender = CUILSender
        self.CUILReceiver = CUILReceiver
        self.evento = evento
        self.fechaDeEnvio = datetime.now()

    def solicitudAEscrbir(self):
        return [str(self.CUILSender), str(self.CUILReceiver), str(self.evento), str(self.fechaDeEnvio)]