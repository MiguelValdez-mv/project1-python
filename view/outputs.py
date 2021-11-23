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


def print_file_upload_indications():
    print("📥 Cargar Archivo")
    print("\nIndicaciones:\n")
    print("1. El archivo debe estar ubicado en la carpeta 'files' del proyecto")
    print("2. El formato del archivo debe ser '.txt'")
    print("3. Por cada competidor se debe especificar de manera obligatoria la siguiente información: Cédula, 1er Apellido, 2do Apellido, Nombre, Inicial 2do Nombre, Sexo, Edad, Horas, Minutos y Segundos")
    print("4. El archivo suministrado debe contener en cada línea la información de cada competidor separada por comas")
    print("5. En el momento que se le solicite, introduzca el nombre del archivo junto con su extensión. Por ejemplo: nombre_archivo.txt")
