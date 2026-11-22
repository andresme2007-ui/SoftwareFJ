import logging
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva
class GestorSistema:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
    def registrar_cliente(self, cliente):
        if any(c.identificador == cliente.identificador
               for c in self.clientes):
            raise ErrorCliente("El cliente ya existe")
        self.clientes.append(cliente)
        logging.info("Cliente registrado correctamente")
    def registrar_servicio(self, servicio):
        if any(s.identificador == servicio.identificador
               for s in self.servicios):
            raise ErrorServicio("El servicio ya existe")
        self.servicios.append(servicio)
        logging.info("Servicio registrado correctamente")
    def registrar_reserva(self, reserva):
        if any(r.identificador == reserva.identificador
               for r in self.reservas):
            raise ErrorReserva("La reserva ya existe")
        self.reservas.append(reserva)
        logging.info("Reserva registrada correctamente")
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
    def mostrar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir_servicio())
    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(
                reserva.identificador,
                reserva.cliente.nombre,
                reserva.servicio.nombre,
                reserva.estado
            )