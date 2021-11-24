from constants import COMPETITOR_ATTRIBUTES
from results import utils


def print_competitor_details(competitor={}):
    competitor_details = [
        f"{COMPETITOR_ATTRIBUTES[key]}: {competitor[key]}" for key in list(competitor.keys())
    ]
    print(", ".join(competitor_details))


def print_competitors_table(list_title, competitors=[]):
    format_text = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10}"

    print("\n" + list_title + "\n")
    print(format_text.format(*list(COMPETITOR_ATTRIBUTES.values())) + "\n")

    for competitor in competitors:
        print(format_text.format(*list(competitor.values())))


def print_list_all_competitors(competitors=[]):
    print_competitors_table("🧒 Lista de participantes:", competitors)


def print_total_number_competitors(competitors=[]):
    print("\n📊 Cantidad total de participantes\n")
    print(
        f"La cantidad total de participantes es de: {len(competitors)} participante(s)"
    )


def print_number_competitors_per_age_group(competitors=[]):
    format_text = "{:<10}" * 3
    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )

    print("\n📊 Cantidad de participantes por grupo etario\n")
    print(format_text.format("JUNIORS", "SENIORS", "MASTERS") + "\n")
    print(format_text.format(len(juniors), len(seniors), len(masters)))


def print_number_competitors_per_sex(competitors=[]):
    mens, womens = utils.get_competitors_per_sex(competitors)

    print("\n📊 Cantidad de participantes por sexo\n")
    print(
        f"HOMBRES: {len(mens)} participante(s), MUJERES: {len(womens)} participante(s)"
    )


def print_overall_winner(competitors=[]):
    winner = utils.get_winner(competitors)

    print("\n🏆 Ganador general\n")
    print_competitor_details(winner)


def print_histogram_competitors_per_age_group(competitors=[]):
    juniors, seniors, masters = utils.get_competitors_list_per_age_group(
        competitors
    )

    print("\n📈 Histograma de participantes por grupo etario\n")
    print(f"Juniors ({len(juniors)}): {'*' * int(len(juniors) / 2)}")
    print(f"Seniors ({len(seniors)}): {'*' * int(len(seniors) / 2)}")
    print(f"Masters ({len(masters)}): {'*' * int(len(masters) / 2)}")
