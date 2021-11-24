import file_handler
import constants
from results import outputs

results_menu_options = {
    "list_competitors": outputs.print_list_all_competitors,
    "number_competitors": outputs.print_total_number_competitors,
    "number_competitors_per_age_group": outputs.print_number_competitors_per_age_group,
    "number_competitors_per_sex": outputs.print_number_competitors_per_sex,
    "winners_per_age_group": outputs.print_winners_per_age_group,
    "winners_per_sex": outputs.print_winners_per_sex,
    "winners_per_age_group_and_sex": outputs.print_winners_per_age_group_and_sex,
    "overall_winner": outputs.print_overall_winner,
    "histogram_competitors_per_age_group": outputs.print_histogram_competitors_per_age_group,
}


def print_menu_question(question):
    """
    Imprime una pregunta tipo menú junto con sus posibles respuestas

    Parámetros
    ----------
    question (dictionary): Diccionario con el nombre, titulo, respuestas de la pregunta 

    Retorna
    -------
    str: Cadena con la opción seleccionada
    """

    len_options = len(question["options"])

    print(f"\n{question['title']}\n")

    for idx, option in enumerate(question["options"]):
        print(f"{idx + 1}. {option['message']}")

    while True:
        try:
            selected_option_idx = int(
                input(f"\n➡ Presione un número del 1 al {len_options}: ")
            )

            if 1 <= selected_option_idx <= len_options:
                return question["options"][selected_option_idx - 1]["value"]
            else:
                print(
                    f"❎ Introduzca una opción dentro de los límites establecidos (1..{len_options})"
                )

        except ValueError:
            print("❎ Ingrese un número entero...")


def exit_menu():
    """Muestra un mensaje al salir del programa"""

    print("\nHasta luego 👋😎")
    exit()


def main_menu():
    """Muestra el menú principal del programa"""

    competitors = []

    while True:
        selected_main_menu_option = print_menu_question(
            constants.MAIN_MENU_QUESTION
        )

        if (selected_main_menu_option == "file"):
            selected_file_menu_option = None

            while selected_file_menu_option != "return_to_main_menu":

                selected_file_menu_option = print_menu_question(
                    constants.FILE_MENU_QUESTION
                )

                if (selected_file_menu_option == "file_upload"):
                    competitors = file_handler.load_competition_results()

                elif (selected_file_menu_option == "exit"):
                    exit_menu()

                selected_file_menu_option = print_menu_question(
                    constants.CONTINUE_MENU_QUESTION
                )

        elif (selected_main_menu_option == "results"):
            selected_results_menu_option = None

            while selected_results_menu_option != "return_to_main_menu":
                selected_results_menu_option = print_menu_question(
                    constants.RESULTS_MENU_QUESTION
                )

                results_menu_options[selected_results_menu_option](competitors)

                selected_results_menu_option = print_menu_question(
                    constants.CONTINUE_MENU_QUESTION
                )
