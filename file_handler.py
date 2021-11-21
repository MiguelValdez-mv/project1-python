from io import open

def load_competition_results():
	file = open("./files/competencia.txt", "r")
	lines = file.readlines()
	print(lines)
	file.close()