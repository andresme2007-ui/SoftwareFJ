from abc import ABC, abstractmethod
class Entidad(ABC):
    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificado es obligatorio")
        self._identificador = identificador
    @property
    def identificador(self):
        return self._identificador
    @abstractmethod
    def mostrar_informacion(self):
        pass