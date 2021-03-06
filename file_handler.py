from io import open
from exceptions import InvalidFileFormat, InvalidColumnsNumber
from constants import COMPETITOR_ATTRIBUTES


def load_competition_results():
    """
    Lee los resultados de la competenci贸n dado el nombre
    de un archivo dentro de la carpeta 'file'

    Retorna
    -------
    list: Lista de diccionarios con la informaci贸n de cada competidor
    """

    competitors = []
    competitor_keys_list = list(COMPETITOR_ATTRIBUTES.keys())

    print("馃摜 Cargar Archivo")
    print("\nIndicaciones:\n")
    print("1. El archivo debe estar ubicado en la carpeta 'files' del proyecto")
    print("2. El formato del archivo debe ser '.txt'")
    print("3. Por cada competidor se debe especificar de manera obligatoria la siguiente informaci贸n: C茅dula, 1er Apellido, 2do Apellido, Nombre, Inicial 2do Nombre, Sexo, Edad, Horas, Minutos y Segundos")
    print("4. El archivo suministrado debe contener en cada l铆nea la informaci贸n de cada competidor separada por comas")
    print("5. En el momento que se le solicite, introduzca el nombre del archivo junto con su extensi贸n. Por ejemplo: nombre_archivo.txt")

    while True:
        try:
            file_name = input(
                "\n鉃? Introduzca el nombre del archivo usando el formato nombre_archivo.extensi贸n: "
            )

            if not file_name.endswith(".txt"):
                raise InvalidFileFormat

            file = open(f"./files/{file_name}", "r")
            lines = file.readlines()
            file.close()

            for idx, line in enumerate(lines):
                competitor_data_list = line.replace("\n", "").split(",")

                if(
                    len(competitor_data_list) != len(competitor_keys_list) or
                    False in map(lambda item: bool(item), competitor_data_list)
                ):
                    raise InvalidColumnsNumber(line, idx + 1)

                competitors.append({
                    key: value for key, value in zip(
                        competitor_keys_list, competitor_data_list
                    )
                })

            print("\n鉁? Los datos de la competici贸n han sido cargados exitosamente...")

            return competitors
        except (InvalidFileFormat, InvalidColumnsNumber) as e:
            print(e)
        except FileNotFoundError:
            print("鉂? El archivo no existe en el directorio files...")
