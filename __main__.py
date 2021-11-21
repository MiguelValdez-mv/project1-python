from view import questions as qn, outputs as o
from file_handler import load_competition_results

def exit_project():
	print("\nHasta luego 👋😎")
	exit()

def continue_menu():
	if (not o.print_menu_question(qn.continue_question)):
		exit_project()

def main():
	participants = None
	selected_option = None

	while True:
		selected_option = o.print_menu_question(qn.main_menu_question)

		if (selected_option == "file"):
			selected_option = o.print_menu_question(qn.file_menu_question)

			if (selected_option == "file_upload"):
				participants = load_competition_results()
			
			elif (selected_option == "exit"):
				exit_project()

			continue_menu()
		elif (selected_option == "results"):
			selected_option = o.print_menu_question(qn.results_menu_question)
			
			continue_menu()
		
if __name__ == "__main__":
	main()
