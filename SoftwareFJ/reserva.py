import logging
from excepciones import ErrorReserva, ServicioNoDisponible
class Reserva:
    def __init__(self, identificador, cliente, servicio, duracion):
        if cliente is None:
            raise ErrorReserva("Debe existir un cliente")
        if servicio is None:
            raise ErrorReserva("Debe existir un servicio")
        servicio.validar_parametros(duracion)
        self.identificador = identificador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
    def confirmar(self):
        try:
            if self.estado != "Pendiente":
                raise ErrorReserva("La reserva no puede confirmarse")
            self.estado = "Confirmada"
            logging.info(f"Reserva {self.identificador} confirmada")
        except ErrorReserva as error:
            logging.error(str(error))
            raise
    def cancelar(self):
        try:
            if self.estado != "Pendiente" and self.estado != "Confirmada":
                raise ErrorReserva("No se puede cancelar esta reserva")
            self.estado = "Cancelada"
            logging.info(f"Reserva {self.identificador} cancelada")
        except ErrorReserva as error:
            logging.error(str(error))
            raise
    def procesar(self):
        try:
            if self.estado != "Confirmada":
                raise ServicioNoDisponible(
                    "La reserva debe estar confirmada"
                )
            costo = self.servicio.calcular_costo(self.duracion)
            return costo
        except Exception as error:
            logging.error(f"Error procesando reserva: {error}")
            raise ErrorReserva("No fue posible procesar la reserva") from error