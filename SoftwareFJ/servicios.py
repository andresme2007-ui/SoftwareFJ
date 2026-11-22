from abc import ABC, abstractmethod
from excepciones import ErrorServicio
class Servicio(ABC):
    def __init__(self, identificador, nombre, precio):
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            raise ErrorServicio("El precio debe ser positivo")
        if not nombre or not nombre.strip():
            raise ErrorServicio("El nombre es obligatorio")
        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio
    @abstractmethod
    def calcular_costo(self, cantidad):
        pass
    @abstractmethod
    def describir_servicio(self):
        pass
    @abstractmethod
    def validar_parametros(self, cantidad):
        pass
class ReservaSala(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ErrorServicio("Horas inválidas")
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_parametros(cantidad)
        self.validar_tarifas(impuesto, descuento)
        subtotal = self.precio * cantidad
        return subtotal * (1 + impuesto) * (1 - descuento)
    def validar_tarifas(self, impuesto, descuento):
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise ErrorServicio("Impuesto o descuento inválido")
    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"
class AlquilerEquipo(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ErrorServicio("Cantidad de equipos inválida")
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_parametros(cantidad)
        self.validar_tarifas(impuesto, descuento)
        return self.precio * cantidad * (1 + impuesto) * (1 - descuento)
    def validar_tarifas(self, impuesto, descuento):
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise ErrorServicio("Impuesto o descuento inválido")
    def describir_servicio(self):
        return f"Alquiler de equipos: {self.nombre}"
class Asesoria(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ErrorServicio("Duración de asesoría inválida")
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_parametros(cantidad)
        self.validar_tarifas(impuesto, descuento)
        return self.precio * cantidad * (1 + impuesto) * (1 - descuento)
    def validar_tarifas(self, impuesto, descuento):
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise ErrorServicio("Impuesto o descuento inválido")
    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"