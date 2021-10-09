from abc import ABC, abstractmethod


class Usuarios(ABC):

    @abstractmethod
    def __init__(self,CUIL,telefono):
        self.CUIL = CUIL
        self.telefono = telefono




