import file_handler
import constants
from results import outputs

results_menu_options = {
    "list_competitors": outputs.print_list_all_competitors,
    "number_competitors": outputs.print_total_number_competitors,
    "number_competitors_per_age_group": outputs.print_number_competitors_per_age_group,
    "number_competitors_per_sex": outputs.print_number_competitors_per_sex,
    "histogram_competitors_per_age_group": outputs.print_histogram_competitors_per_age_group,
    "overall_winner": outputs.print_overall_winner
}


def print_menu_question(question):
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
    print("\nHasta luego 👋😎")
    exit()


def continue_menu():
    if (not print_menu_question(constants.CONTINUE_MENU_QUESTION)):
        exit_menu()


def main_menu():
    competitors = []

    while True:
        selected_option = print_menu_question(constants.MAIN_MENU_QUESTION)

        if (selected_option == "file"):
            selected_option = print_menu_question(constants.FILE_MENU_QUESTION)

            if (selected_option == "file_upload"):
                competitors = file_handler.load_competition_results()

            elif (selected_option == "exit"):
                exit_menu()

            continue_menu()
        elif (selected_option == "results"):
            selected_option = print_menu_question(
                constants.RESULTS_MENU_QUESTION
            )

            results_menu_options[selected_option](competitors)

            continue_menu()
