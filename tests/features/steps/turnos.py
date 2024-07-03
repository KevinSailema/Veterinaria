from behave import *
from app.modelos import *

use_step_matcher("re")



@step('que existen "{turnos_existentes:d}" turnos tomados en un día particular')
def step_impl(context, turnos_existentes):
    día = 1
    context.veterinaria = Veterinaria()
    for numero_turnos in range(turnos_existentes):
        context.veterinaria.agregar_turno(TipoTurno.VACUNACION, Mascota("Firulais"),día)
    assert len(context.veterinaria.obtener_turnos(día)) == turnos_existentes

@step("se solicita un turno para vacunación en un espacio disponible")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se solicita un turno para vacunación en un espacio disponible')


@step('se "(.+)" el turno y quedan "(?P<turnos_disponibles>.+)" turnos disponibles')
def step_impl(context, arg0, turnos_disponibles):
    """
    :type context: behave.runner.Context
    :type arg0: str
    :type turnos_disponibles: str
    """
    raise NotImplementedError(
        u'STEP: Entonces se "<estado_asignación>" el turno y quedan "<turnos_disponibles>" turnos disponibles')


@step('que existen "0" turnos disponibles en un día en particular')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que existen "0" turnos disponibles en un día en particular')


@step("se solicita un turno de emergencia")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se solicita un turno de emergencia')


