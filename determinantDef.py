import LinearAlgebraPurePython as la
from cypherDef import solve_cypher_caesar


def solve_determinant(question):
	p = question.find("Caesar's code")
	if p >= 0:
		question = solve_cypher_caesar(question, "determinant")
	pre_matrix = question.split('\\')
	array = []

	for i in pre_matrix:
		array.append((i.split('&')))

	array = list(filter(lambda a: a != [''], array))
	for i in range(len(array)):
		for j in range(len(array[i])):
			array[i][j] = int(array[i][j])
	return la.determinant_recursive(array)