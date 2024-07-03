from enum import Enum


class TipoTurno(Enum):
    EMERGENCIA = 1
    VACUNACION = 2
    CONSULTA_GENERAL = 3
    PELUQUERIA = 4

class Veterinaria:
    def agregar_turno(self, VACUNACION, param, día):
        pass

    def obtener_turnos(self, día):
        pass

class Mascota:
    pass

