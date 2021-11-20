main_menu_question = {
	"type": "list",
  "name": "main_menu",
  "message": "Menú principal:",
  "choices": [
	  {
	    "name": "📂 Archivo",
	    "value": "file"
	  },
    {
      "name": "📊 Resultados",
      "value": "results"
    },
  ]
}

file_menu_question = {
	"type": "list",
  "name": "file_menu",
  "message": "Menú Archivo:",
  "choices": [
	  {
	    "name": "📥 Cargar Archivo",
	    "value": "file_upload"
	  },
    {
      "name": "🚪 Salir",
      "value": "exit"
    },
  ]
}

results_menu_question = {
	"type": "list",
  "name": "results_menu",
  "message": "Menú Resultados:",
  "choices": [
	  {
	    "name": "🧒 Lista de participantes",
	    "value": "list_participants"
	  },
	  {
	    "name": "📊 Cantidad total de participantes",
	    "value": "number_participants"
	  },
	  {
	    "name": "📊 Cantidad de participantes por grupo etario",
	    "value": "number_participants_per_age_group"
	  },
	  {
	    "name": "📊 Cantidad de participantes por sexo",
	    "value": "number_participants_per_sex"
	  },
	  {
	    "name": "🏆 Ganadores por grupo etario",
	    "value": "winners_per_age_group"
	  },
	  {
	    "name": "🏆 Ganadores por sexo",
	    "value": "winners_per_sex"
	  },
	  {
	    "name": "🏆 Ganadores por grupo etario y sexo",
	    "value": "winners_per_age_group_and_sex"
	  },
	  {
	    "name": "🏆 Ganador general",
	    "value": "overall_winner"
	  },
	  {
	    "name": "📈 Histograma de participantes por grupo etario",
	    "value": "histogram_participants_per_age_group"
	  },
  ]
}

continue_question = {
	"type": "confirm",
	"name": "continue_question",
  "message": "🤔 ¿Desea regresar al Menú Principal?",
  "default": False,
};