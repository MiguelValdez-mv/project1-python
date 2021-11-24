"""
Pregunta del menú prinicipal de la aplicación

Contiene el nombre del menú, el título que será mostrado en consola
junto con las posibles respuestas/opciones a ser seleccioanadas por el usuario
"""
MAIN_MENU_QUESTION = {
    "name": "main_menu",
    "title": "Menú principal:",
    "options": [
        {
            "message": "📂 Archivo",
            "value": "file"
        },
        {
            "message": "📊 Resultados",
            "value": "results"
        },
    ]
}

"""Pregunta del menú archivo"""
FILE_MENU_QUESTION = {
    "name": "file_menu",
    "title": "Menú Archivo:",
    "options": [
        {
            "message": "📥 Cargar Archivo",
            "value": "file_upload"
        },
        {
            "message": "🚪 Salir",
            "value": "exit"
        },
    ]
}

"""Pregunta del menú resultados"""
RESULTS_MENU_QUESTION = {
    "name": "results_menu",
    "title": "Menú Resultados:",
    "options": [
        {
            "message": "🧒 Lista de participantes",
            "value": "list_competitors"
        },
        {
            "message": "📊 Cantidad total de participantes",
            "value": "number_competitors"
        },
        {
            "message": "📊 Cantidad de participantes por grupo etario",
            "value": "number_competitors_per_age_group"
        },
        {
            "message": "📊 Cantidad de participantes por sexo",
            "value": "number_competitors_per_sex"
        },
        {
            "message": "🏆 Ganadores por grupo etario",
            "value": "winners_per_age_group"
        },
        {
            "message": "🏆 Ganadores por sexo",
            "value": "winners_per_sex"
        },
        {
            "message": "🏆 Ganadores por grupo etario y sexo",
            "value": "winners_per_age_group_and_sex"
        },
        {
            "message": "🏆 Ganador general",
            "value": "overall_winner"
        },
        {
            "message": "📈 Histograma de participantes por grupo etario",
            "value": "histogram_competitors_per_age_group"
        },
    ]
}

"""Pregunta del menú continuar"""
CONTINUE_MENU_QUESTION = {
    "name": "continue_menu",
    "title": "¿Desea regresar al Menú Principal?:",
    "options": [
        {"message": "✅ Sí", "value": "return_to_main_menu"},
        {"message": "❎ No", "value": "stay_in_current_menu"}
    ],
}

"""Contiene todos los atributos de un competidor"""
COMPETITOR_ATTRIBUTES = {
    "ci": "CÉDULA",
    "first_last_name": "1º APELLIDO",
    "second_last_name": "2º APELLIDO",
    "name": "NOMBRE",
    "middle_initial": "I.2º NOMBRE",
    "sex": "SEXO",
    "age": "EDAD",
    "hours": "HORAS",
    "minutes": "MINUTOS",
    "seconds": "SEGUNDOS"
}

"""Géneros de los competidores"""
SEXES = {
    "MALE": "M",
    "FEMALE": "F",
}
