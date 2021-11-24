from constants import COMPETITOR_ATTRIBUTES
from results import utils


def print_competitor_details(competitor={}):
    """
    Imprime los detalles de un competidor en una sola línea

    Parámetros
    ----------
    competitor (dictionary): Información del competidor        
    """

    competitor_details = [
        f"{COMPETITOR_ATTRIBUTES[key]}: {competitor[key]}" for key in list(competitor.keys())
    ]
    print(", ".join(competitor_details))


def print_competitors_table(list_title, competitors=[]):
    """
    Imprime una tabla de competidores

    Parámetros
    ----------
    list_title (str): Título de la tabla
    competitors (list): Lista de competidores   
    """

    if(utils.list_competitors_is_empty(competitors)):
        return

    format_text = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}"

    print("\n" + list_title + "\n")
    print(format_text.format(*list(COMPETITOR_ATTRIBUTES.values())) + "\n")

    for competitor in competitors:
        print(format_text.format(*list(competitor.values())))


def print_list_all_competitors(competitors=[]):
    """
    Imprime una tabla de todos los competidores registrados

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    print_competitors_table("🧒 Lista de participantes:", competitors)


def print_total_number_competitors(competitors=[]):
    """
    Imprime la cantidad total de participantes registrados

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    print("\n📊 Cantidad total de participantes\n")
    print(
        f"La cantidad total de participantes es de: {len(competitors)} participante(s)"
    )


def print_number_competitors_per_age_group(competitors=[]):
    """
    Imprime la cantidad de competidores registrados por grupo etario

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    format_text = "{:<10}" * 3
    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )

    print("\n📊 Cantidad de participantes por grupo etario\n")
    print(format_text.format("JUNIORS", "SENIORS", "MASTERS") + "\n")
    print(format_text.format(len(juniors), len(seniors), len(masters)))


def print_number_competitors_per_sex(competitors=[]):
    """
    Imprime la cantidad de competidores registrados por sexo

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    mens, womens = utils.get_competitors_per_sex(competitors)

    print("\n📊 Cantidad de participantes por sexo\n")
    print(
        f"HOMBRES: {len(mens)} participante(s), MUJERES: {len(womens)} participante(s)"
    )


def print_winners_per_age_group(competitors=[]):
    """
    Imprime los ganadores de la competición por grupo etario

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    if(utils.list_competitors_is_empty(competitors)):
        return

    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )
    winners_per_age_group = [
        utils.get_winner(juniors),
        utils.get_winner(seniors),
        utils.get_winner(masters),
    ]

    print_competitors_table(
        "🏆 Ganadores por grupo etario", winners_per_age_group
    )


def print_winners_per_sex(competitors=[]):
    """
    Imprime los ganadores de la competición por sexo

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    if(utils.list_competitors_is_empty(competitors)):
        return

    mens, womens = utils.get_competitors_per_sex(competitors)
    winners_per_sex = [
        utils.get_winner(mens),
        utils.get_winner(womens),
    ]

    print_competitors_table(
        "🏆 Ganadores por sexo", winners_per_sex
    )


def print_winners_per_age_group_and_sex(competitors=[]):
    """
    Imprime los ganadores de la competición por grupo etario y sexo

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    if(utils.list_competitors_is_empty(competitors)):
        return

    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )
    winners_per_age_group_and_sex = map(
        utils.get_winner,
        list(
            utils.get_competitors_per_sex(juniors) +
            utils.get_competitors_per_sex(seniors) +
            utils.get_competitors_per_sex(masters)
        ),
    )

    print_competitors_table(
        "🏆 Ganadores por grupo etario y sexo", winners_per_age_group_and_sex
    )


def print_overall_winner(competitors=[]):
    """
    Imprime el ganador general de la competición

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    if(utils.list_competitors_is_empty(competitors)):
        return

    winner = utils.get_winner(competitors)

    print("\n🏆 Ganador general\n")
    print_competitor_details(winner)


def print_histogram_competitors_per_age_group(competitors=[]):
    """
    Imprime el historigrama de los competidores registrados por grupo
    etario

    Parámetros
    ----------
    competitors (list): Lista de competidores   
    """

    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )

    print("\n📈 Histograma de participantes por grupo etario\n")
    print(f"Juniors ({len(juniors)}): {'*' * int(len(juniors) / 2)}")
    print(f"Seniors ({len(seniors)}): {'*' * int(len(seniors) / 2)}")
    print(f"Masters ({len(masters)}): {'*' * int(len(masters) / 2)}")
