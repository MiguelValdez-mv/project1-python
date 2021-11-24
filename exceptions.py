class InvalidFileFormat(Exception):
    """
    Excepción originada cuando el usuario cargue 
    un archivo cuyo formato sea diferente a '.txt'
    """

    def __init__(self):
        super().__init__(
            "❎ El formato del archivo suministrado no es válido. Por favor, cargue un archivo '.txt'"
        )


class InvalidColumnsNumber(Exception):
    """
    Excepción originada cuando se detecte que un competidor
    no tiene todos los datos requeridos tales como: Cédula,
    1er apellido, 2do apellido, nombre, inicial segundo nombre,
    sexo, edad, horas, minutos y segundo.
    """

    def __init__(self, line, line_number):
        """   
        Parámetros
        ----------
        line (str): Línea que contiene al competidor con los datos incompletos
        line_number (int): Número de línea que contiene al competidor con los datos incompletos
        """

        super().__init__(
            f"❎ La línea Nº{line_number} del archivo suministrado no posee la información requerida completa del competidor\n\n➡ {line}"
        )
