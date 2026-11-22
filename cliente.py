import re
from entidades import Entidad
from excepciones import ErrorCliente
class Cliente(Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        if not nombre or not nombre.strip():
            raise ErrorCliente("El nombre es obligatorio")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", correo):
            raise ErrorCliente("Correo electrónico inválido")
        if not telefono.isdigit() or len(telefono) < 7:
            raise ErrorCliente("Teléfono inválido")
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
    @property
    def nombre(self):
        return self.__nombre
    @property
    def correo(self):
        return self.__correo
    @property
    def telefono(self):
        return self.__telefono
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )