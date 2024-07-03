# Created by kevin at 3/7/24

# language: es
Característica: Asignación de turnos
  Como Veterinaria
  quiero que los clientes puedan ser atendidos por turnos diarios de atención, dando prioridad
  para aminorar la carga de trabajo y mejorar la atención a los clientes.


  Esquema del escenario: Asignación de turnos con espacios disponibles
    Dado que existen "<turnos_existentes>" turnos tomados en un día particular
    Cuando se solicita un turno para vacunación en un espacio disponible
    Entonces se "<estado_asignación>" el turno y quedan "<turnos_disponibles>" turnos disponibles
    Ejemplos:
      | turnos_existentes | estado_asignación | turnos_disponibles |
      |         2         |      asigna       |         2          |
      |         5         |      rechaza      |         0          |

  Escenario: Asignación de turnos de emergencia
    Dado que existen "0" turnos disponibles en un día en particular
    Cuando se solicita un turno de emergencia
    Entonces se "asigna" el tuirno y quedan "0" turnos disponibles