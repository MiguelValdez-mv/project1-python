from datetime import time
from constants import SEXES


def list_competitors_is_empty(competitors=[]):
    """
    Valida si una lista de competidores está vacía y muestra en mensaje
    si ese es el caso

    Parámetros
    ----------
    competitors (list): Lista de competidores

    Retorna
    -------
    bool: True si la lista de competidores está vacía, False en caso contrario
    """

    if(not competitors):
        print("\nActualmente no hay participantes registrados...")
        return True

    return False


def is_junior_competitor(competitor={}):
    """
    Valida si un competidor es junior (iguales o menores a 25 años)

    Parámetros
    ----------
    competitor (dictionary): Información del competidor

    Retorna
    -------
    bool: True si el competidor es junior, False en caso contrario
    """

    return int(competitor["age"]) <= 25


def is_senior_competitor(competitor={}):
    """
    Valida si un competidor es senior (mayores de 25 y menores o iguales a 40 años)

    Parámetros
    ----------
    competitor (dictionary): Información del competidor

    Retorna
    -------
    bool: True si el competidor es senior, False en caso contrario
    """

    return 25 < int(competitor["age"]) <= 40


def is_master_competitor(competitor={}):
    """
    Valida si un competidor es master (mayores de 40 años)

    Parámetros
    ----------
    competitor (dictionary): Información del competidor

    Retorna
    -------
    bool: True si el competidor es master, False en caso contrario
    """

    return 40 < int(competitor["age"])


def is_male_competitor(competitor={}):
    """
    Valida si un competidor es de sexo masculino

    Parámetros
    ----------
    competitor (dictionary): Información del competidor

    Retorna
    -------
    bool: True si el competidor es de sexo masculino, False en caso contrario
    """

    return competitor["sex"] == SEXES["MALE"]


def is_female_competitor(competitor={}):
    """
    Valida si un competidor es de sexo femenino

    Parámetros
    ----------
    competitor (dictionary): Información del competidor

    Retorna
    -------
    bool: True si el competidor es de sexo femenino, False en caso contrario
    """

    return competitor["sex"] == SEXES["FEMALE"]


def get_competitors_list_per_age_group(competitors=[]):
    """
    Clasifica a los competidores por grupo etario

    Parámetros
    ----------
    competitors (list): Lista de competidores

    Retorna
    -------
    tuple: Tupla con la lista de competidores juniors, seniors y masters
    """

    juniors = []
    seniors = []
    masters = []

    for competitor in competitors:
        if(is_junior_competitor(competitor)):
            juniors.append(competitor)
        elif(is_senior_competitor(competitor)):
            seniors.append(competitor)
        elif(is_master_competitor(competitor)):
            masters.append(competitor)

    return juniors, seniors, masters


def get_competitors_per_sex(competitors=[]):
    """
    Clasifica a los competidores por sexo

    Parámetros
    ----------
    competitors (list): Lista de competidores

    Retorna
    -------
    tuple: Tupla con la lista de competidores masculinos y femeninos
    """

    mens = []
    womens = []

    for competitor in competitors:
        if(is_male_competitor(competitor)):
            mens.append(competitor)
        elif(is_female_competitor(competitor)):
            womens.append(competitor)

    return mens, womens


def get_winner(competitors=[]):
    """
    Determina el competidor ganador dada una lista de competidores

    Parámetros
    ----------
    competitors (list): Lista de competidores

    Retorna
    -------
    dictionary: Competidor ganador
    """

    return min(
        competitors,
        key=lambda c: time(
            int(c["hours"]), int(c["minutes"]), int(c["seconds"])
        )
    )
