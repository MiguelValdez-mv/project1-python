from io import open
from view.outputs import print_file_upload_indications
from exceptions import InvalidFileFormat, InvalidColumnsNumber

competitors_keys = [
    "ci",
    "first_last_name",
    "second_last_name",
    "name",
    "middle_initial",
    "sex",
    "age",
    "hours",
    "minutes",
    "seconds"
]


def load_competition_results():
    competitors = []

    print_file_upload_indications()

    while True:
        try:
            file_name = input(
                "\n➡ Introduzca el nombre del archivo usando el formato nombre_archivo.extensión: "
            )

            if not file_name.endswith(".txt"):
                raise InvalidFileFormat

            file = open(f"./files/{file_name}", "r")
            lines = file.readlines()
            file.close()

            for idx, line in enumerate(lines):
                competitor_data_list = line.replace("\n", "").split(",")

                if(
                    len(competitor_data_list) != len(competitors_keys) or
                    False in map(lambda item: bool(item), competitor_data_list)
                ):
                    raise InvalidColumnsNumber(line, idx + 1)

                competitors.append({
                    key: value for key, value in zip(
                        competitors_keys, competitor_data_list
                    )
                })

            print("\n✅ Los datos de la competición han sido cargados exitosamente...")

            return competitors
        except (InvalidFileFormat, InvalidColumnsNumber) as e:
            print(e)
        except FileNotFoundError as e:
            print("❎ El archivo no existe en el directorio files...")
