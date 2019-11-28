import numpy as np
import LinearAlgebraPurePython as la
from determinantDef import solve_determinant
from cypherDef import solve_cypher_caesar


def matrix_minor(A, i, j):
    return np.delete(np.delete(A,i,axis=0), j, axis=1)

def solve_inverse(question):

	p = question.find("Caesar's code")
	if p >= 0:
		question = solve_cypher_caesar(question, "inverse-matrix")

	pre_matrix = question.split('\\')
	array = []
	answer = ""

	for i in pre_matrix:
		array.append((i.split('&')))

	array = list(filter(lambda a: a != [''], array))
	for i in range(len(array)):
		for j in range(len(array[i])):
			array[i][j] = int(array[i][j])
	determinant = la.determinant_recursive(array)
	if la.check_non_singular(array) and abs(determinant) >= 1e-9:
		"""
		invA = []
	    
		for i in range(len(array)):
			tmpArray = []
			for j in range(len(array)):
				minor = matrix_minor(array,i,j)
				tmpArray.append(((-1) ** (i + j)) * np.linalg.det(minor))
			invA.append(tmpArray)

		invA = np.transpose(invA)
		for i in range(len(invA)):
			for j in range(len(invA)):
				invA[i][j] = round(invA[i][j]/determinant)
		value = invA
		"""
		value = np.linalg.inv(array)
	else:
		return "unsolvable"

	for i in range(len(value)):
		for j in range(len(value[i])):
			answer += str(value[i][j])
			if j + 1 < len(value[i]):
				answer += " & "
		if i + 1 < len(value):
			answer += " \\\\ "

	return answer