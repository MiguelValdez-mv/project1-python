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

CONTINUE_MENU_QUESTION = {
    "name": "continue_menu",
    "title": "¿Desea regresar al Menú Principal?:",
    "options": [
        {"message": "✅ Sí", "value": True},
        {"message": "❎ No", "value": False}
    ],
}

COMPETITOR_ATTRIBUTES = {
    "ci": "Cédula",
    "first_last_name": "1er Apellido",
    "second_last_name": "2do Apellido",
    "name": "Nombre",
    "middle_initial": "Inicial 2do Nombre",
    "sex": "Sexo",
    "age": "Edad",
    "hours": "Horas",
    "minutes": "Minutos",
    "seconds": "Segundos"
}
