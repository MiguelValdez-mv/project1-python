class InvalidFileFormat(Exception):
    def __init__(self):
        super().__init__(
            "❎ El formato del archivo suministrado no es válido. Por favor, cargue un archivo '.txt'"
        )


class InvalidColumnsNumber(Exception):
    def __init__(self, line, line_number):
        super().__init__(
            f"❎ La línea Nº{line_number} del archivo suministrado no posee la información requerida completa del competidor\n\n➡ {line}"
        )
