# Dependencias de terceros
from PyInquirer import prompt

# Dependencias propias del proyecto
from view import questions as qn
from file_handler import load_competition_results

def exit_project():
	print("Hasta luego 👋😎")
	exit()

def continue_menu():
	if (not prompt(qn.continue_question)["continue_question"]):
		exit_project()

def main():
	participants = None
	selected_option = None

	while True:
		selected_option = prompt(qn.main_menu_question)["main_menu"]

		if (selected_option == "file"):
			selected_option = prompt(qn.file_menu_question)["file_menu"]

			if (selected_option == "file_upload"):
				participants = load_competition_results()
			
			elif (selected_option == "exit"):
				exit_project()

			continue_menu()
		elif (selected_option == "results"):
			selected_option = prompt(qn.results_menu_question)["results_menu"]
			
			continue_menu()

		
if __name__ == "__main__":
	main()
