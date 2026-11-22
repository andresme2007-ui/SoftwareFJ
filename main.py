import os
import logging
import math
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from gestor import GestorSistema
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
sistema = GestorSistema()


def ejecutar_pruebas():
    """Ejecuta las pruebas del sistema y devuelve el gestor utilizado."""
    global sistema
    sistema = GestorSistema()
    print("\n===== SISTEMA SOFTWARE FJ =====")
    try:
        cliente1 = Cliente(
            "C001", "Andres Mejia",
            "Andresme2007@gmail.com", "3219769091"
        )
        sistema.registrar_cliente(cliente1)
        print("1. Cliente registrado")
    except Exception as error:
        logging.exception("Error en prueba 1")
        print("1. Error:", error)
    try:
        Cliente("C002", "Ana", "correo_invalido", "123")
    except Exception as error:
        logging.exception("Error en prueba 2")
        print("2. Cliente inválido:", error)
    try:
        cliente2 = Cliente(
            "C003", "Ximena Mejia",
            "Andrea2004villarrealmejia@gmail.com", "3222443436"
        )
        sistema.registrar_cliente(cliente2)
        print("3. Segundo cliente registrado")
    except Exception as error:
        logging.exception("Error en prueba 3")
        print("3. Error:", error)
    try:
        sala = ReservaSala("S001", "Sala principal", 50000)
        sistema.registrar_servicio(sala)
        print("4. Sala creada")
    except Exception as error:
        logging.exception("Error en prueba 4")
        print("4. Error:", error)
    try:
        equipo = AlquilerEquipo("S002", "Proyector", 30000)
        sistema.registrar_servicio(equipo)
        print("5. Equipo creado")
    except Exception as error:
        logging.exception("Error en prueba 5")
        print("5. Error:", error)
    try:
        asesoria = Asesoria("S003", "Asesoría informática", 80000)
        sistema.registrar_servicio(asesoria)
        print("6. Asesoría creada")
    except Exception as error:
        logging.exception("Error en prueba 6")
        print("6. Error:", error)
    try:
        ReservaSala("S004", "Sala inválida", -500)
    except Exception as error:
        logging.exception("Error en prueba 7")
        print("7. Servicio inválido:", error)
    try:
        Reserva("R001", None, sala, 2)
    except Exception as error:
        logging.exception("Error en prueba 8")
        print("8. Reserva inválida:", error)
    try:
        reserva1 = Reserva("R002", cliente1, sala, 2)
        sistema.registrar_reserva(reserva1)
        reserva1.confirmar()
        costo = reserva1.procesar()
        print("9. Reserva confirmada. Costo:", costo)
    except Exception as error:
        logging.exception("Error en prueba 9")
        print("9. Error:", error)
    try:
        reserva2 = Reserva("R003", cliente2, equipo, 2)
        sistema.registrar_reserva(reserva2)
        reserva2.confirmar()
        reserva2.cancelar()
        print("10. Reserva cancelada")
    except Exception as error:
        logging.exception("Error en prueba 10")
        print("10. Error:", error)
    print("\n===== CLIENTES =====")
    sistema.mostrar_clientes()
    print("\n===== SERVICIOS =====")
    sistema.mostrar_servicios()
    print("\n===== RESERVAS =====")
    sistema.mostrar_reservas()


def _leer_numero_positivo(mensaje, entero=False):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada) if entero else float(entrada)
            if not math.isfinite(valor) or valor <= 0:
                raise ValueError("El valor debe ser un número positivo")
            return valor
        except ValueError as error:
            print("Entrada inválida:", error)


def _buscar_por_identificador(elementos, identificador, tipo):
    for elemento in elementos:
        if elemento.identificador == identificador:
            return elemento
    raise ValueError(f"No se encontró {tipo} con identificador {identificador}")


def _registrar_cliente():
    identificador = input("Identificador del cliente: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo electrónico: ").strip()
    telefono = input("Teléfono: ").strip()
    cliente = Cliente(identificador, nombre, correo, telefono)
    sistema.registrar_cliente(cliente)
    print("Cliente registrado correctamente.")


def _registrar_servicio():
    print("Tipo de servicio: 1. Sala  2. Alquiler de equipo  3. Asesoría")
    tipo = input("Seleccione el tipo: ").strip()
    clases_servicio = {
        "1": ReservaSala,
        "2": AlquilerEquipo,
        "3": Asesoria,
    }
    clase_servicio = clases_servicio.get(tipo)
    if clase_servicio is None:
        raise ValueError("Tipo de servicio inválido")

    identificador = input("Identificador del servicio: ").strip()
    nombre = input("Nombre del servicio: ").strip()
    precio = _leer_numero_positivo("Precio: ")
    servicio = clase_servicio(identificador, nombre, precio)
    sistema.registrar_servicio(servicio)
    print("Servicio registrado correctamente.")


def _crear_reserva():
    identificador = input("Identificador de la reserva: ").strip()
    id_cliente = input("Identificador del cliente: ").strip()
    cliente = _buscar_por_identificador(sistema.clientes, id_cliente, "cliente")
    id_servicio = input("Identificador del servicio: ").strip()
    servicio = _buscar_por_identificador(sistema.servicios, id_servicio, "servicio")
    cantidad_entera = isinstance(servicio, AlquilerEquipo)
    mensaje = "Cantidad de equipos: " if cantidad_entera else "Duración: "
    duracion = _leer_numero_positivo(mensaje, entero=cantidad_entera)
    reserva = Reserva(identificador, cliente, servicio, duracion)
    sistema.registrar_reserva(reserva)
    print("Reserva creada correctamente.")


def _buscar_reserva():
    identificador = input("Identificador de la reserva: ").strip()
    return _buscar_por_identificador(sistema.reservas, identificador, "reserva")


def ejecutar_menu_interactivo():
    while True:
        print(
            "\n===== MENÚ INTERACTIVO =====\n"
            "1. Registrar cliente\n"
            "2. Registrar servicio\n"
            "3. Crear reserva\n"
            "4. Confirmar reserva\n"
            "5. Cancelar reserva\n"
            "6. Consultar clientes\n"
            "7. Consultar servicios\n"
            "8. Consultar reservas\n"
            "0. Volver al menú inicial"
        )
        try:
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "0":
                return
            if opcion == "1":
                _registrar_cliente()
            elif opcion == "2":
                _registrar_servicio()
            elif opcion == "3":
                _crear_reserva()
            elif opcion == "4":
                reserva = _buscar_reserva()
                reserva.confirmar()
                print("Reserva confirmada.")
            elif opcion == "5":
                reserva = _buscar_reserva()
                reserva.cancelar()
                print("Reserva cancelada.")
            elif opcion == "6":
                if sistema.clientes:
                    sistema.mostrar_clientes()
                else:
                    print("No hay clientes registrados.")
            elif opcion == "7":
                if sistema.servicios:
                    sistema.mostrar_servicios()
                else:
                    print("No hay servicios registrados.")
            elif opcion == "8":
                if sistema.reservas:
                    sistema.mostrar_reservas()
                else:
                    print("No hay reservas registradas.")
            else:
                print("Opción inválida. Intente nuevamente.")
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo del menú interactivo.")
            return
        except Exception as error:
            logging.exception("Error en el menú interactivo")
            print("No se pudo completar la operación:", error)


def main():
    global sistema
    while True:
        print(
            "\n===== SOFTWARE FJ =====\n"
            "1. Ejecutar menú interactivo\n"
            "2. Ejecutar las 10 pruebas automáticas\n"
            "3. Salir"
        )
        try:
            opcion = input("Seleccione una opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nHasta luego.")
            return

        if opcion == "1":
            sistema = GestorSistema()
            ejecutar_menu_interactivo()
        elif opcion == "2":
            ejecutar_pruebas()
        elif opcion == "3":
            print("Hasta luego.")
            return
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()