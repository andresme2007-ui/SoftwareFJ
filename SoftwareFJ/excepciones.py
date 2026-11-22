class ErrorCliente(Exception):
    """Error relacionado con el cliente."""
    pass


class ErrorServicio(Exception):
    """Error relacionado con el servicio."""
    pass


class ErrorReserva(Exception):
    """Error relacionado con la reserva."""
    pass


class ServicioNoDisponible(Exception):
    """El servicio no esta disponible."""
    pass


class ErrorDatos(Exception):
    """Error en los datos dados."""
    pass