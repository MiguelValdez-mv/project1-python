def print_menu_question(question):
	len_options = len(question["options"])

	print(f"\n{question['title']}\n")

	for idx, option in enumerate(question["options"]):
		print(f"{idx + 1}. {option['message']}")

	while True:
		try:
			selected_option_idx = int(
				input(f"\nPresione un número del 1 al {len_options}: ")
			)
			
			if 1 <= selected_option_idx <= len_options:
				return question["options"][selected_option_idx - 1]["value"]
			else:
				print(
					f"❎ Introduzca una opción dentro de los límites establecidos (1..{len_options})"
				)

		except ValueError:
			print("❎ Ingrese un número entero...")

