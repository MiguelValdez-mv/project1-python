from view import questions as qn, outputs
from file_handler import load_competition_results


def exit_project():
    print("\nHasta luego 👋😎")
    exit()


def continue_menu():
    if (not outputs.print_menu_question(qn.continue_question)):
        exit_project()


def main():
    while True:
        selected_option = outputs.print_menu_question(qn.main_menu_question)

        if (selected_option == "file"):
            selected_option = outputs.print_menu_question(
                qn.file_menu_question
            )

            if (selected_option == "file_upload"):
                competitors = load_competition_results()

            elif (selected_option == "exit"):
                exit_project()

            continue_menu()
        elif (selected_option == "results"):
            selected_option = outputs.print_menu_question(
                qn.results_menu_question
            )

            continue_menu()


if __name__ == "__main__":
    main()
